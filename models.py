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
    pass
