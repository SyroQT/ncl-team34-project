from firebase_admin import db


def get_role_from_id(uid):
    """Returns the role from the given ID token"""
    ref = db.reference("/roles/")
    db_roles = ref.get()
    if uid in list(db_roles["user"].values()):
        return "user"
    elif uid in list(db_roles["admin"].values()):
        return "admin"
