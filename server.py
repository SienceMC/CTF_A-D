import flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
# import sqlite3
from datetime import datetime
# import os
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.sqlite3'
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
    team1 = db.Column(db.Boolean)
    team2 = db.Column(db.Boolean)

    def __repr__(self):
        return '<Task %r>' % self.id


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5))
    points = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id

# db.create_all()

@app.route("/")
def menu():
    return render_template('index.html')


@app.route("/6C02828918114740F1A100B38EEB78B1396F80EEED6AA98EF2222D9BAD6BC158")
def team1():
    return render_template('team_1.html')


@app.route("/75490bd7b93e6fa7d18cfdea90cc6bcb983d5f3ea326249d2709ca6c94bc07ba", methods=["POST"])
def submit():
    flag = flask.request.form.get("Flag")
    team = flask.request.form.get("Team")
    if int(team) == 1:
        flagsthatarethesameastheeingegebeneflaginputimfau = Flags.query.filter_by(
            flag=flag).all()

        # flaggedflags = flagthatshit("team1")
    elif int(team) == 2:
        pass
        # flaggedflags = flagthatshit("team2")
    return flagsthatarethesameastheeingegebeneflaginputimfau


@app.route("/2C57B47A189B1BD3944A039FCD7EC6D872F2BFB3FEDA68A6BFE3DD326F650A64")
def team2():
    return render_template('team_2.html')


@app.route("/nimda")
def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run(port=80, debug=True)
