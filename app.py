import os

from flask import Flask, render_template, request, jsonify, redirect, url_for
from firebase_admin import db, credentials, initialize_app
from dotenv import load_dotenv
from werkzeug.utils import redirect

load_dotenv()
MAP_TOKEN = os.getenv("MAP_TOKEN")
DB_URL = os.getenv("DB_URL")

app = Flask(__name__)

# Firestore setup
# Docs https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
cred = credentials.Certificate("firebase_key.json")
default_app = initialize_app(
    cred,
    {"databaseURL": DB_URL},
)
ref = db.reference("/")

# Token for map API
token = MAP_TOKEN

# dummy data which should be retrieved from DB
issues = [
    {  # Helix Sq
        "lng": -1.6268,
        "lat": 54.9729,
        "color": "black",
        "id": 363,
        "description": "This is a description",
        "category": "Environmental",
        "score": 500,
    },
    {  # USB
        "lng": -1.62494,
        "lat": 54.9735751,
        "color": "blue",
        "id": 696,
        "description": "This is a description",
        "category": "Lights",
        "score": 555,
    },
    {  # The Catalyst
        "lng": -1.6244480090820115,
        "lat": 54.97322654028629,
        "color": "blue",
        "id": 35,
        "description": "This is a description",
        "category": "Lights",
        "score": 55,
    },
    {  # FDC
        "lng": -1.6251856666991449,
        "lat": 54.973163909898304,
        "color": "red",
        "id": 6,
        "description": "This is a description",
        "category": "Cars",
        "score": 42,
    },
]
categories = ["Environmental", "Lights", "Cars", "Wildlife", "Bike lanes"]
# ref.set({"issues": issues, "categories": categories})


# Main view - for now an empty map
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


# Logout handler
@app.route("/logout")
def logout():
    return "Logout"


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")


# User view of the app
@app.route("/user", methods=["POST", "GET"])
def user():
    # Get categories from DB
    ref = db.reference("/categories")
    categories = ref.get()

    # Get issues from db
    ref = db.reference("/issues")
    issues = ref.get()

    return render_template(
        "user.html", token=token, issues=issues, categories=categories
    )


# Admin view of the app
@app.route("/admin", methods=["POST", "GET"])
def admin():
    # Get categories from DB
    ref = db.reference("/categories")
    categories = ref.get()

    # Get issues from db
    ref = db.reference("/issues")
    issues = ref.get()

    return render_template(
        "admin.html", token=token, issues=issues, categories=categories
    )


# Place where new issue data is sent
@app.route("/new_issue", methods=["POST"])
def new_issue():
    ref = db.reference("/issues")
    issues = ref.get()
    id = 1 + len(issues)

    new_issue = {
        "category": request.form["category"],
        "color": "black",
        "description": request.form["description"],
        "lng": request.form["lng"],
        "lat": request.form["lat"],
        "score": 1,
        "id": id,
    }

    ref.push(new_issue)
    return redirect(url_for("user"))


# Place where new issue data is sent
@app.route("/score_cast", methods=["POST"])
def score_cast():
    # TODO: track user ids to not allow users vote multiple times
    ref = db.reference("/issues/")
    issues = ref.get()

    for k, v in issues.items():
        if v["id"] == int(request.form["issue-id"]):
            ref.child(k).update({"score": int(request.form["score"])})

    return redirect(url_for("user"))


# About page
@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":

    app.run(debug=True)
