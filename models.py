from app import mysql as db


class Category(db.Model):
    __tablename__ = "Categories"

    category = db.Column(db.String(100), primary_key=True)

    def __init__(self, category):
        self.category = category


class Issue(db.Model):
    __tablename__ = "Issue"

    id = db.Column(db.Integer, primary_key=True)
    creator_user = db.Column(db.String(20), db.ForeignKey("Users.username"))
    category = db.Column(db.String(100), db.ForeignKey("Categories.category"))

    location = db.Column(db.String(100))
    description = db.Column(db.String(100))
    created_time = db.Column(db.DateTime)
    resolved_time = db.Column(db.DateTime)
    is_resolved = db.Column(db.Boolean)
    votes = db.Column(db.Integer)

    #  Relationships with other tables
    users = db.relationship('User', foreign_keys=[creator_user])
    categories = db.relationship("Category", foreign_keys=[category])

    def __init__(self, location, description, category, created_time, resolved_time, is_resolved=False, votes=0):
        self.location = location
        self.description = description
        self.category = category
        self.created_time = created_time
        self.resolved_time = resolved_time
        self.is_resolved = is_resolved
        self.votes = votes


class User(db.Model):
    __tablename__ = "Users"

    username = db.Column(db.String(20), primary_key=True)

    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    # issues = db.relationship('Issue')

    def __init(self, username, firstname, lastname, email, password, phone_number, isAdmin):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.isAdmin = isAdmin


def init_db():
    print("Delete DB")
    db.drop_all()
    print("Create DB")
    db.create_all()

    # Add main categories
    categories = ["Environmental", "Lights", "Cars", "Wildlife", "Bike lanes"]
    for item in categories:
        db.session.add(Category(item))
    db.session.commit()
