import os

from firebase_admin import db
from dotenv import load_dotenv
from flask import Blueprint, render_template, redirect, url_for, request

from Functions import requiresRoles

"""
Views related to admin role:
- delete_issue
- admin

"""

admins_blueprints = Blueprint("admins", __name__, template_folder="templates")

load_dotenv()
MAP_TOKEN = os.getenv("MAP_TOKEN")

# Deletes an issue
@admins_blueprints.route("/delete_issue", methods=["POST"])
@requiresRoles.requires_roles("admin")
def delete_issue():
    ref = db.reference("/issues/")
    issues = ref.get()
    for k, v in issues.items():
        if v["id"] == int(request.form["issue-id"]):
            ref.child(k).set({})
    return redirect(url_for("admins.admin"))


# Admin view of the app
@admins_blueprints.route("/admin", methods=["POST", "GET"])
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
        "admin.html", token=MAP_TOKEN, issues=issues, categories=categories
    )
