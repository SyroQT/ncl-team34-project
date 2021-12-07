import json
import re

from flask import Flask, render_template

app = Flask(__name__)

# Token for map API
token = "pk.eyJ1Ijoic3lyb3F0IiwiYSI6ImNrd2d1M2dwOTBzMHoyd21vaXUwemZsZHYifQ.qMKLv7M4w6lRtfaDopK73A"


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    # dummy data which should be retrieved from DB
    issues = [
        {  # Helix Sq
            "location": [-1.6268, 54.9729],
            "color": "black",
            "id": 363,
            "description": "This is a description",
            "category": "This is the category",
            "upvotes": 500,
            "downvotes": 60,
        },
        {  # USB
            "location": [-1.62494, 54.9735751],
            "color": "blue",
            "id": 696,
            "description": "This is a description",
            "category": "This is the category",
            "upvotes": 555,
            "downvotes": 600,
        },
    ]
    return render_template("user.html", token=token, issues=issues)


if __name__ == "__main__":
    app.run(debug=True)
