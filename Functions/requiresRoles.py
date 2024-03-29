import json
from functools import wraps
from time import sleep
from logging import raiseExceptions

from firebase_admin import auth, db
from flask import session, render_template

"""
Decorator file:
- required_roles -> checks if the user has authorisation to visit the route
"""


def requires_roles(role=None):
    """Checks if the user session contains a valid token and if it has the correct role.
    If no role is given then only checks for the valid token.
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):

            try:
                sleep(0.05)
                verif = auth.verify_id_token(json.loads(session["idToken"]))
            except:
                verif = {}
            if "uid" in verif.keys():
                try:
                    ref = db.reference("/roles/")
                    db_roles = ref.get()
                    if not role:
                        return f(*args, **kwargs)
                    elif verif["uid"] in list(db_roles[role].values()):
                        # print(
                        #     verif["uid"] in list(db_roles[role].values()),
                        #     db_roles,
                        #     "\n" + role,
                        #     f,
                        # )
                        return f(*args, **kwargs)
                    else:
                        raiseExceptions("TypeError")
                except:
                    # TODO: create the template
                    # return render_template("403.html")
                    return render_template("403.html")
            else:
                # TODO: create the template
                # return render_template("403.html")
                return render_template("403.html")

        return wrapped

    return wrapper
