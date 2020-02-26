import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'

class Flags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))

    # https://youtu.be/Z1RJmh_OqeA?t=1115


@app.route("/")
def menu():
    return \
        """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        .dropbtn {
        background-color: #3498DB;
        color: white;
        padding: 16px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        }

        .dropbtn:hover, .dropbtn:focus {
        background-color: #2980B9;
        }

        .center{
            text-align: center;
        }
        .dropdown {
        position: relative;
        display: inline-block;
        }

        .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f1f1f1;
        min-width: 160px;
        overflow: auto;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
        }

        .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        }

        .dropdown a:hover {background-color: #ddd;}

        .show {display: block;}
        </style>
        </head>
        <body>

        <h2 class="center">Attack and Defense CTF</h2>
        <p class="center">Please select your Team for submitting Flags.</p>
        <center>
        <div class="dropdown">
        <button onclick="myFunction()" class="dropbtn">Dropdown</button>
        <div id="myDropdown" class="dropdown-content">
            <a href="/6C02828918114740F1A100B38EEB78B1396F80EEED6AA98EF2222D9BAD6BC158">Team 1</a>
            <a href="/2C57B47A189B1BD3944A039FCD7EC6D872F2BFB3FEDA68A6BFE3DD326F650A64">Team 2</a>
            <a href="https://heeeeeeeey.com/">Admin</a>
        </div>
        </div>
        </center>
        <script>
        /* When the user clicks on the button, 
        toggle between hiding and showing the dropdown content */
        function myFunction() {
        document.getElementById("myDropdown").classList.toggle("show");
        }

        // Close the dropdown if the user clicks outside of it
        window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            var i;
            for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
            }
        }
        }
        </script>

        </body>
        </html>

        """

@app.route("/6C02828918114740F1A100B38EEB78B1396F80EEED6AA98EF2222D9BAD6BC158")
def team1():
    return "You are currently in Team 1"

@app.route("/2C57B47A189B1BD3944A039FCD7EC6D872F2BFB3FEDA68A6BFE3DD326F650A64")
def team2():
    return "You are currently in Team 2"