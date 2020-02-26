import flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
db = SQLAlchemy(app)

class Flags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    points = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id
    


@app.route("/")
def menu():
    return render_template('index.html')

@app.route("/6C02828918114740F1A100B38EEB78B1396F80EEED6AA98EF2222D9BAD6BC158")
def team1():
    return render_template('team_1.html')

@app.route("/2C57B47A189B1BD3944A039FCD7EC6D872F2BFB3FEDA68A6BFE3DD326F650A64")
def team2():
    return render_template('team_2.html')