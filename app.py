import json
import os
import requests

from dotenv import load_dotenv
from firebase_admin import db, credentials, initialize_app, auth
from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect


from Functions import requiresRoles, getRoleFromID

# TODO:
# refactor the code
# style it a bit
# error handling
# error pages
# about page

# proper id system for issues
# testing


# from users.forms import RegisterForm, LoginForm


load_dotenv()
MAP_TOKEN = os.getenv("MAP_TOKEN")
DB_URL = os.getenv("DB_URL")
API_KEY = os.getenv("API_KEY")
FLASK_SECRET = os.getenv("FLASK_SECRET")

app = Flask(__name__)
app.config["SECRET_KEY"] = FLASK_SECRET

# Firestore setup
# Docs https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/
cred = credentials.Certificate("firebase_key.json")
default_app = initialize_app(
    cred,
    {"databaseURL": DB_URL},
)
ref = db.reference(path="/")


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

# this deletes all data from db so be careful
# ref.set({"issues": issues, "categories": categories})


# Main view redirects to login
@app.route("/")
def index():
    return redirect("login")


@app.route("/login", methods=["POST", "GET"])
def login():
    """auth is being implemented according to this website
    https://blog.icodes.tech/posts/python-firebase-authentication.html
    """
    if request.method == "POST":

        details = {
            "email": request.form["email"],
            "password": request.form["password"],
            "returnSecureToken": True,
        }
        # Post request to firebase api
        r = requests.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}".format(
                API_KEY
            ),
            data=details,
        )
        # check for errors
        # TODO error handling
        if "error" in r.json().keys():
            response = {"status": "error", "message": r.json()["error"]["message"]}

        # success
        if "idToken" in r.json().keys():
            response = {"status": "success", "idToken": r.json()["idToken"]}
            session["idToken"] = json.dumps(response["idToken"])

            verif = auth.verify_id_token(response["idToken"])
            user_type = getRoleFromID.get_role_from_id(verif["uid"])
            return redirect(url_for(user_type))

    return render_template("login.html")


# Logout handler
@app.route("/logout")
@requiresRoles.requires_roles()
def logout():
    session["idToken"] = None
    return redirect("login")


# Register route
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # TODO: validation of data
        details = {
            "email": request.form["email"],
            "password": request.form["password"],
            "returnSecureToken": True,
        }
        # send post request to firebase api
        r = requests.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}".format(
                API_KEY
            ),
            data=details,
        )
        # check for errors in result]\
        # TODO error handling
        if "error" in r.json().keys():
            response = {"status": "error", "message": r.json()["error"]["message"]}
        # if the registration succeeded
        if "idToken" in r.json().keys():
            response = {"status": "success", "idToken": r.json()["idToken"]}
            session["idToken"] = json.dumps(response["idToken"])

            # save int the db that a new user is registered
            verif = auth.verify_id_token(response["idToken"])
            ref = db.reference("/roles/user/")
            ref.push(verif["uid"])

            return redirect(url_for("user"))

    return render_template("register.html")


# User view of the app
@app.route("/user", methods=["POST", "GET"])
@requiresRoles.requires_roles("user")
def user():
    # Get categories from DB
    ref = db.reference("/categories")
    categories = ref.get()

    # Get issues from db
    ref = db.reference("/issues/")
    issues = ref.get()
    if type(issues) == list:
        issues = [i for i in issues if i]
    else:
        issues = {k: v for k, v in issues.items() if v is not None}

    return render_template(
        "user.html", token=token, issues=issues, categories=categories
    )


# Admin view of the app
@app.route("/admin", methods=["POST", "GET"])
@requiresRoles.requires_roles("admin")
def admin():
    # Get categories from DB
    ref = db.reference("/categories/")
    categories = ref.get()

    # Get issues from db
    ref = db.reference("/issues/")
    issues = ref.get()
    if type(issues) == list:
        issues = [i for i in issues if i]
    else:
        issues = {k: v for k, v in issues.items() if v is not None}

    return render_template(
        "admin.html", token=token, issues=issues, categories=categories
    )


# Place where new issue data is sent
@app.route("/new_issue", methods=["POST"])
@requiresRoles.requires_roles("user")
def new_issue():
    ref = db.reference("/issues")
    issues = ref.get()
    # TODO : needs a better way of calculating ids
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
@requiresRoles.requires_roles("user")
def score_cast():
    # TODO: track user ids to not allow users vote multiple times
    ref = db.reference("/issues/")
    issues = ref.get()

    for k, v in issues.items():
        if v["id"] == int(request.form["issue-id"]):
            ref.child(k).update({"score": int(request.form["score"])})

    return redirect(url_for("user"))


# Deletes an issue
@app.route("/delete_issue", methods=["POST"])
@requiresRoles.requires_roles("admin")
def delete_issue():
    ref = db.reference("/issues/")
    issues = ref.get()
    for k, v in issues.items():
        if v["id"] == int(request.form["issue-id"]):
            ref.child(k).set({})

    return redirect(url_for("admin"))


# About page
@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    app.run(debug=True)
