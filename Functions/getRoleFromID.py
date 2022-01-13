from firebase_admin import db


def get_role_from_id(uid):
    """Checks wich role is the given token user"""
    ref = db.reference("/roles/")
    db_roles = ref.get()
    if uid in list(db_roles["user"].values()):
        return "user"
    elif uid in list(db_roles["admin"].values()):
        return "admin"