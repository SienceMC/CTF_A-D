import flask
from flask import render_template, redirect
from flask_sqlalchemy import SQLAlchemy
# import sqlite3
from datetime import datetime
# import os
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
# teams = SQLAlchemy(app)
# db = sqlite3.connect("ctf.db")
# cursor = db.cursor()
# def flagthatshit(team):
#     flaggedflags = cursor.execute(f"""SELECT * FROM teams WHERE name="{team}" """)
# Not Working for some Reason:

# Database.execute("""CREATE TABLE flags (
#     flag text,
#     points integer
#     )""")


# Database.create("flags", ("id INTEGER NOT NULL PRIMARY KEY", ))


class Flags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flag = db.Column(db.String(200))
    points = db.Column(db.Integer)
    teams = db.Column(db.String(1000), default="")
    
    def __repr__(self):
        return '<Flag %r>' % self.id

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5))
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Team %r>' % self.id

# db.create_all()

@app.route("/")
def menu():
    return render_template('index.html', teams=Teams.query.all())

@app.route("/capture", methods=["POST"])
def submit():
    flag = flask.request.form.get("Flag")
    team = flask.request.form.get("Team")
    team = Teams.query.filter_by(name = team).first()
    flaged = Flags.query.filter_by(flag = flag).first()
    try:
        if team.name not in flaged.teams:
            try:
                db.session.delete(team)
                db.session.delete(flaged)
                flaged.teams += team.name
                team.points += flaged.points
                db.session.add(team)
                db.session.add(flaged)
                db.session.commit()
            except:
                return "<h1>OH CRAP!</h1><h2>There was an error occured!</h2>"
            finally:
                return f"<h1>SUBMITTED!</h1><h2>YOUR TEAMS' SCORE's now: {team.points}</h2>"
        elif team.name in flaged.teams:
            print(f"INFO: Detected multiple submission from team { team.id }")
            return "<h1>YOU LITTLE...</h1><h2>You really tried to enter a flag two times?</h2>"
    except:
        return render_template('false_flag.html')
    # flaggedflags = flagthatshit("team1")
        
        # flaggedflags = flagthatshit("team2")
    return str(flaged)


@app.route("/team/<int:id>", methods=['GET'])
def team(id):
    return render_template('team.html', team=Teams.query.filter_by(id=id).first())


@app.route("/nimda", methods=['GET', 'POST'])
def admin():
    if flask.request.method == "POST":
        if flask.request.form.get("request") == "teamadd":
            newteam = Teams(name=f"team{len(Teams.query.all())+1}")
            db.session.add(newteam)
            db.session.commit()
        elif flask.request.form.get("request") == "flagadd":
            print("Flagadd recived")
            newflag = Flags(flag=flask.request.form.get("flag"))
            newflag.points = flask.request.form.get("points")
            db.session.add(newflag)
            db.session.commit()
        # elif flask.request.form.get("request") == "teamdelete":
        #     team = Teams.query.filter_by(id=flask.request.form.get("team")).first()
        #     print(team)
        #     db.session.remove(team)
        #     db.session.commit()
        elif flask.request.form.get("request") == "flagdelete":
            flag = Flags.query.filter_by(id = flask.request.form.get("flag")).all()
            db.session.remove(flag)
            db.session.commit()
    return render_template('admin.html', teams=Teams.query.all(), flags=Flags.query.all())

@app.route('/deleteteam/<int:id>')
def delete(id):
    team_to_delete = Teams.query.get_or_404(id)

    try:
        db.session.delete(team_to_delete)
        db.session.commit()
        return redirect('/nimda')
    except:
        return 'There was a problem deleting that Team'

@app.route('/deleteflag/<int:id>')
def delete_(id):
    flag_to_delete = Flags.query.get_or_404(id)

    try:
        db.session.delete(flag_to_delete)
        db.session.commit()
        return redirect('/nimda')
    except:
        return 'There was a problem deleting that Flag'



if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=80, debug=True)
