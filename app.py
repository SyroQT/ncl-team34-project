import json
import re

from flask import Flask, render_template, request, flash
from users.forms import RegisterForm, LoginForm

app = Flask(__name__)

# Token for map API
# Will have to put it in the env variable or smt
token = "pk.eyJ1Ijoic3lyb3F0IiwiYSI6ImNrd2d1M2dwOTBzMHoyd21vaXUwemZsZHYifQ.qMKLv7M4w6lRtfaDopK73A"

# dummy data which should be retrieved from DB
issues = [
    {  # Helix Sq
        "location": [-1.6268, 54.9729],
        "color": "black",
        "id": 363,
        "description": "This is a description",
        "category": "Environmental",
        "upvotes": 500,
        "downvotes": 60,
    },
    {  # USB
        "location": [-1.62494, 54.9735751],
        "color": "blue",
        "id": 696,
        "description": "This is a description",
        "category": "Lights",
        "upvotes": 555,
        "downvotes": 600,
    },
    {  # The Catalyst
        "location": [-1.6244480090820115, 54.97322654028629],
        "color": "blue",
        "id": 35,
        "description": "This is a description",
        "category": "Lights",
        "upvotes": 55,
        "downvotes": 6,
    },
    {  # FDC
        "location": [-1.6251856666991449, 54.973163909898304],
        "color": "red",
        "id": 6,
        "description": "This is a description",
        "category": "Cars",
        "upvotes": 42,
        "downvotes": 69,
    },
]
categories = ["Environmental", "Lights", "Cars", "Wildlife", "Bike lanes"]


# Main view - for now an empty map
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    return render_template("login.html", form=form)


# Logout handler
@app.route("/logout")
def logout():
    return "Logout"


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(request.form.get('email'))
        print(request.form.get('password'))

        return login()
    return render_template("register.html", form=form)


# User view of the app
@app.route("/user", methods=["POST", "GET"])
def user():
    return render_template(
        "user.html", token=token, issues=issues, categories=categories
    )


# Admin view of the app
@app.route("/admin", methods=["POST", "GET"])
def admin():
    return render_template(
        "admin.html", token=token, issues=issues, categories=categories
    )


# Place where new issue data is sent
@app.route("/new_issue", methods=["POST"])
def new_issue():
    print(request.form)
    return "New issue is taken care of"


# About page
@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True)
