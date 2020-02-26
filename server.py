import flask
from flask import render_template
# from flask_sqlalchemy import SQLAlchemy
import sqlite3
from datetime import datetime

app = flask.Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
# db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
# teams = SQLAlchemy(app)

class Database:
    def __init__(self, db):
        self.db = sqlite3.connect(db)
        self.cursor = self.db.cursor()
    #hippety hoppety get off my property!
    def execute(self, what):
        self.cursor.execute(what)

# Not Working for some Reason:

# Database.execute("""CREATE TABLE flags (
#     flag text,
#     points integer
#     )""")


# Database.create("flags", ("id INTEGER NOT NULL PRIMARY KEY", ))


# class Flags(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200))
#     points = db.Column(db.Integer)

#     def __repr__(self):
#         return '<Task %r>' % self.id
    


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
    return "<h1>SUBMITTED!!!!!!!!!!!!!!!!</h1>"
@app.route("/2C57B47A189B1BD3944A039FCD7EC6D872F2BFB3FEDA68A6BFE3DD326F650A64")
def team2():
    return render_template('team_2.html')
@app.route("/nimda")
def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run(port=80, debug=True)