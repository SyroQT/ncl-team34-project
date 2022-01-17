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


if __name__ == "__main__":
    from users.views import users_blueprint
    from admins.views import admins_blueprints
    from standard.views import standard_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(admins_blueprints)
    app.register_blueprint(standard_blueprint)
    app.run(debug=True)
