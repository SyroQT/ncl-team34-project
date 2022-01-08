import json

import requests
from firebase_admin import auth, db
from flask import Blueprint, request, session, redirect, url_for, render_template

standardPages_blueprint = Blueprint('StandardPages', __name__, template_folder='templates')

from app import API_KEY
# Main view redirects to login
# TODO : Index page
@standardPages_blueprint.route("/")
def index():
    return redirect("login")


# About page
# TODO : about page
@standardPages_blueprint.route("/about")
def about():
    return "About"


# Register route
@standardPages_blueprint.route("/register", methods=["POST", "GET"])
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
