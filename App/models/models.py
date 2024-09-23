from App.database import db
from werkzeug.security import check_password_hash, generate_password_hash

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50),nullable=False)
    jobTitle =  db.Column(db.String(60), nullable=False, unique=True)

    def __init__(self, company, jobTitle):
        self.company = company
        self.jobTitle = jobTitle

    def get_json(self):
        return{
            'id': self.id,
            'company': self.company,
            'jobTitle': self.jobTitle
        }

class JobApplications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.id'),nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('applicant.id'),nullable=False)
    
    def __init__(self,jobID,userID):
        self.jobID = jobID
        self.userID = userID

    def get_json(self):
        return{
            'id': self.id,
            'jobID': self.jobID,
            'userID': self.userID
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName =  db.Column(db.String(90), nullable=False)
    lName = db.Column(db.String(90), nullable=False)
    
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def get_json(self):
        return{
            'id': self.id,
            'fName': self.fName,
            'lName': self.lName
        }



class Admin(User):
    __tablename__ = 'admin'
    staff_id = db.Column(db.Integer, unique=True)
    __mapper_args__ = {
      'polymorphic_identity': 'admin',
  }

    def __init__(self, staff_id, fName, lName):
        super().__init__(fName, lName)
        self.staff_id = staff_id

class Applicant(User):
    __tablename__ = 'applicant'
    username = db.Column(db.String(80), nullable=False,unique=True)
    password = db.Column(db.String(90), nullable=False)
    __mapper_args__ = {
      'polymorphic_identity': 'applicants',
    }

    def __init__(self, fName, lName, username,password):
        super().__init__(fName, lName)
        self.username = username
        self.password = set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)