from flask import render_template
from app import app

@app.route("/")
def home():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Meep morp human noises!'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'I too am a human!'
        }
    ]
    return render_template("home.html", title="test title", posts=posts)

@app.route("/index")
def index():
    return render_template("index.html", title="\"Home\"")