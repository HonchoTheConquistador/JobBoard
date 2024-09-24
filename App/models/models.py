from App.database import db
from werkzeug.security import check_password_hash, generate_password_hash
#from sqlalchemy import func

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False)
    jobTitle = db.Column(db.String(60), nullable=False)

    def __init__(self, company, jobTitle):
        self.company = company
        self.jobTitle = jobTitle

    def get_json(self):
        return {
            'id': self.id,
            'company': self.company,
            'jobTitle': self.jobTitle
        }

class sysUser(db.Model):
    __tablename__ = 'sysuser'
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String(90), nullable=False)
    lName = db.Column(db.String(90), nullable=False)
    type = db.Column(db.String(50))
    __mapper_args__ = {'polymorphic_identity': 'sysuser', 'polymorphic_on': type}

    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def get_json(self):
        return {
            'id': self.id,
            'fName': self.fName,
            'lName': self.lName
        }

class Admin(sysUser):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('sysuser.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, fName, lName):
        super().__init__(fName, lName)

    def get_json(self):
        return {
            "id": self.id,
            'fName': self.fName,
            'lName': self.lName
        }

class Applicant(sysUser):
    __tablename__ = 'applicant'
    id = db.Column(db.Integer, db.ForeignKey('sysuser.id'), primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'applicant',
    }

    def __init__(self, fName, lName, username, password):
        super().__init__(fName, lName)
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_json(self):
        return {
            "id": self.id,
            'fName': self.fName,
            'lName': self.lName,
            'username': self.username
        }

class JobApplications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('sysuser.id'), nullable=False)
    
    def __init__(self, jobID, userID):
        self.jobID = jobID
        self.userID = userID

    def get_json(self):
        return {
            'id': self.id,
            'jobID': self.jobID,
            'userID': self.userID
        }