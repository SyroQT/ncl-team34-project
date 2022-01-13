import os
import json

import requests
from dotenv import load_dotenv
from firebase_admin import auth, db
from flask import Blueprint, request, session, redirect, url_for, render_template

standard_blueprint = Blueprint("standard", __name__, template_folder="templates")

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Main view redirects to login
@standard_blueprint.route("/")
def index():
    return redirect("login")


# About page
# TODO : about page
@standard_blueprint.route("/about")
def about():
    return "About"


# Register route
@standard_blueprint.route("/register", methods=["POST", "GET"])
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
        if "error" in r.json().keys():
            response = {"status": "error", "message": r.json()["error"]["message"]}
            return render_template("register.html", errors=response["message"])

        # if the registration succeeded
        if "idToken" in r.json().keys():
            response = {"status": "success", "idToken": r.json()["idToken"]}
            session["idToken"] = json.dumps(response["idToken"])

            # save int the db that a new user is registered
            verif = auth.verify_id_token(response["idToken"])
            ref = db.reference("/roles/user/")
            ref.push(verif["uid"])

            return redirect(url_for("users.user"))

    return render_template("register.html", errors=None)
