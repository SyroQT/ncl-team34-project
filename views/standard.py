import json
import os
from flask.helpers import url_for

import requests
from dotenv import load_dotenv
from flask import Blueprint, redirect, request, render_template, session
from firebase_admin import db, credentials, initialize_app, auth

standard_blueprint = Blueprint("standard_blueprint", __name__)


load_dotenv()
MAP_TOKEN = os.getenv("MAP_TOKEN")
DB_URL = os.getenv("DB_URL")
API_KEY = os.getenv("API_KEY")
FLASK_SECRET = os.getenv("FLASK_SECRET")

# Main view redirects to login
@standard_blueprint.route("/")
def index():
    return redirect("login")


# About page
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
            verify=True,
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
