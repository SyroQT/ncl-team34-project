# Decorators
import json
from functools import wraps
from logging import raiseExceptions

from firebase_admin import auth, db
from flask import session


def requires_roles(role=None):
    """Checks if the user session contains a valid token and if it has the correct role.
    If no role is given then only checks for the valid token.
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):

            try:
                verif = auth.verify_id_token(json.loads(session["idToken"]))
            except TypeError:
                verif = {}

            if "uid" in verif.keys():
                try:
                    ref = db.reference("/roles/")
                    db_roles = ref.get()
                    if not role:
                        return f(*args, **kwargs)

                    elif verif["uid"] in list(db_roles[role].values()):
                        return f(*args, **kwargs)
                    else:
                        raiseExceptions("TypeError")

                except:
                    # TODO: create the template
                    # return render_template("403.html")
                    return "Unauthorized"
            else:
                # TODO: create the template
                # return render_template("403.html")
                return "Unauthorized"

        return wrapped

    return wrapper
