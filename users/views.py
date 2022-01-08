import os
import json

import requests
from firebase_admin import auth, db
from dotenv import load_dotenv
from flask import session, redirect, render_template, request, url_for, Blueprint

from Functions import requiresRoles, getRoleFromID


# CONFIG
users_blueprint = Blueprint("users", __name__, template_folder="templates")

load_dotenv()
MAP_TOKEN = os.getenv("MAP_TOKEN")
API_KEY = os.getenv("API_KEY")

# Place where new issue data is sent
@users_blueprint.route("/new_issue", methods=["POST"])
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
    return redirect(url_for("users.user"))


# Place where new issue data is sent
@users_blueprint.route("/score_cast", methods=["POST"])
@requiresRoles.requires_roles("user")
def score_cast():
    # TODO: track user ids to not allow users vote multiple times
    ref = db.reference("/issues/")
    issues = ref.get()

    for k, v in issues.items():
        if v["id"] == int(request.form["issue-id"]):
            ref.child(k).update({"score": int(request.form["score"])})

    return redirect(url_for("users.user"))


# User view of the app
@users_blueprint.route("/user", methods=["POST", "GET"])
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
        "user.html", token=MAP_TOKEN, issues=issues, categories=categories
    )


# User login view
@users_blueprint.route("/login", methods=["POST", "GET"])
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
            if user_type == "user":
                user_type = "users.user"
            else:
                user_type = "admins.admin"
            print(user_type)
            return redirect(url_for(user_type))

    return render_template("login.html")


# User logout view
@users_blueprint.route("/logout")
@requiresRoles.requires_roles()
def logout():
    session["idToken"] = None
    return redirect("login")
