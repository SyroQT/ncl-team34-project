import os

from dotenv import load_dotenv
from firebase_admin import db, credentials, initialize_app
from flask import Flask


# TODO:
# style it a bit
# error pages
# about page
# testing


load_dotenv()
DB_URL = os.getenv("DB_URL")
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


if __name__ == "__main__":
    from users.views import users_blueprint
    from admins.views import admins_blueprints
    from standard.views import standard_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(admins_blueprints)
    app.register_blueprint(standard_blueprint)
    app.run(debug=True)
