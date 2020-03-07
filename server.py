import flask
from flask import render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
# persons = SQLAlchemy(app)
# db = sqlite3.connect("ctf.db")
# cursor = db.cursor()
# def flagthatshit(person):
#     flaggedflags = cursor.execute(f"""SELECT * FROM persons WHERE name="{person}" """)
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
    persons = db.Column(db.String(1000), default="")
    
    def __repr__(self):
        return '<Flag %r>' % self.id

class Persons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Person %r>' % self.id

# db.create_all()

@app.route("/")
def index():
    ranks = []
    people = {}
    for person in Persons.query.all():
        people.update({person.name: person.points})
    people = sorted(people.items(), key=lambda item: item[1], reverse=True)
    for rank, (name, points) in enumerate(people):
        ranks.append([rank+1, name, points])
    return render_template('index.html', ranks=ranks)

@app.route("/capture", methods=["POST"])
def submit():
    flag = flask.request.form.get("Flag")
    person = flask.request.form.get("Person")
    print(person)
    person = Persons.query.filter_by(name = person).first()
    flaged = Flags.query.filter_by(flag = flag).first()
    try:
        if person.name not in flaged.persons:
            try:
                db.session.delete(person)
                db.session.delete(flaged)
                flaged.persons += person.name
                person.points += flaged.points
                db.session.add(person)
                db.session.add(flaged)
                db.session.commit()
            except:
                return "<h1>OH CRAP!</h1><h2>An error occured!</h2>"
            finally:
                print(f"INFO: Flagsubmit recived from {person.name}")
                return f"<h1>SUBMITTED!</h1><h2>YOUR SCORE's now: {person.points}</h2>"
        elif person.name in flaged.persons:
            print(f"INFO: Detected multiple submission from { person.name }")
            return "<h1>YOU LITTLE...</h1><h2>You really tried to enter a flag two times?</h2>"
    except:
        print(f"INFO: False Flagsubmit recived from {person.name}")
        return render_template('false_flag.html')
    # flaggedflags = flagthatshit("person1")
        
        # flaggedflags = flagthatshit("person2")
    return str(flaged)


@app.route("/person", methods=['POST'])
def person():
    name = flask.request.form.get("name")
    print(name)
    print(Persons.query.filter_by(name=name).first())
    if Persons.query.filter_by(name=name).first() == None:
        newperson = Persons(name=name)
        db.session.add(newperson)
        db.session.commit()
        print("INFO: Person added")
    return render_template('person.html', person=Persons.query.filter_by(name=name).first())


@app.route("/nimda", methods=['GET', 'POST'])
def admin():
    if flask.request.method == "POST":  
        if flask.request.form.get("request") == "flagadd":
            print("INFO: Flagadd recived")
            newflag = Flags(flag=flask.request.form.get("flag"))
            newflag.points = flask.request.form.get("points")
            db.session.add(newflag)
            db.session.commit()
        # elif flask.request.form.get("request") == "persondelete":
        #     person = Persons.query.filter_by(id=flask.request.form.get("person")).first()
        #     print(person)
        #     db.session.remove(person)
        #     db.session.commit()
        elif flask.request.form.get("request") == "flagdelete":
            flag = Flags.query.filter_by(id = flask.request.form.get("flag")).all()
            db.session.remove(flag)
            db.session.commit()
            print("INFO: Flagdelete recived")
        return redirect("/nimda")
    else:
        return render_template('admin.html', persons=Persons.query.all(), flags=Flags.query.all())

@app.route('/deleteperson/<name>')
def delete(name):
    person_to_delete = Persons.query.filter_by(name=name).first()

    try:
        db.session.delete(person_to_delete)
        db.session.commit()
        return redirect('/nimda')
    except:
        return 'There was a problem deleting that Person'

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
