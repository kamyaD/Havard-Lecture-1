import datetime
from flask import Flask, render_template, request, session
from Flask-Session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    headline = "Hello, David!"
    return render_template("index.html", headline=headline)

@app.route("/new_year")
def new_year():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)

@app.route("/loops")
def loops():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("names.html", names=names)

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method=="GET":
        return "Please submit the form instead."
    else:
        name=request.form.get("name")
        print(name)
        return render_template("hello.html", name=name)


@app.route("/notes", methods=["GET", "POST"])
def add():
    session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=notes)

