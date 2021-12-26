from app import mysql as db


class Categories(db.Model):
    __tablename__ = "Categories"

    type = db.Column(db.String(100), nullable=False)

    def __init__(self, category):
        self.type = category


class Issue(db.Model):
    pass


class UserIssue(db.Model):
    pass


class Users(db.Model):
    __tablename__ = "Users"

    username = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(11), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, firstname, lastname, email, password, phonenumber, admin):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phonenumber = phonenumber
        self.admin = admin

