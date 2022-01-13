class User:

    def __init__(self, Username, Firstname, Lastname, email, password, PhoneNumber=None, Admin=False):
        self.Username = Username
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.email = email
        self.password = password
        self.PhoneNumber = PhoneNumber
        self.Admin = Admin

    def getName(self):
        return f"{self.Firstname} {self.Lastname}"

    def getEmail(self):
        return self.email
