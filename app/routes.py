from flask import render_template
from app import app

info = {
    "author": "Matt Briggs",
    "title": "H",
    "current_sub": ""
}


@app.route("/")
def home():
    info.update({"title": "Test Title",
                 "current_sub": "/"})
    return render_template("home.html", info=info)


@app.route("/index")
def index():
    info.update({"title": "\"Home\"",
                 "current_sub": "/index"})
    return render_template("index.html", info=info)
