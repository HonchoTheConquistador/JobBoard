from App.models import models
from App.database import db

#create admin 

def create_admin(fName,lName):
    newAdmin = Admin(fName=fName,lName=lName)
    db.session.add(newAdmin)
    db.session.commit()
    return newAdmin

#sign up user

def sign_up_applicant(fName,lName,username,password):
    newApplicant = Applicant(fName=fName,lName=lName,username=username,password=password)
    db.session.add(newApplicant)
    db.session.commit()
    return newApplicant

#apply to job 

def apply_to_job(jobID,userID):
    job = Jobs.query.filter_by(jobID=jobID).first()
    user = Applicant.query.filter_by(id=userID).first()
    if not job or not user:
        print("Error applying to job!!!")
    newJobApplication = JobApplications(jobID,userID)
    allJobs = JobApplications.query.filter_by(jobID=jobID,userID=userID).first()
    if allJobs: #checks to see if the job application exists already
        print("Job application already exists!!!")
        return
    db.session.add(newJobApplication)
    db.session.commit()
    return

#create Job 

def create_job(company,jobTitle):
    job = Jobs(company, jobTitle)
    jobCheck = Jobs.query.filter_by(company=company,jobTitle=jobTitle).first()
    if jobCheck:
        print("Job already exists!!!")
        return
    print("Successfully added a job!")
    db.session.add(job)
    db.session.commit()
    return

#view applicants

def get_all_applicants():
    jobsList = JobApplications.query.all()
    applicants = [job.get_json() for job in jobsList]

#view applicants by job id 
def get_all_applicants_by_jobID(id):
    jobsList = JobApplications.query.filter_by(jobID=id)
    if not jobs:
        print("Error!!!")
        return 
    applicants = [job.get_json() for job in jobsList]
    return applicants

#view applicants by company -------------------------------

def get_applicants_by_company(companyName):
    companyOfferings = Jobs.query.filter_by(company=companyName)
    if not company:
        print("Error finding company!!!")
        return
    #jobsList = [job.get_json() for job in companyOfferings]
    #return jobsList

#view jobs by company 
def get_jobs_by_company(companyName):
    companyOfferings = Jobs.query.filter_by(company=companyName)
    if not company:
        print("Error finding company!!!")
        return
    jobsList = [job.get_json() for job in companyOfferings]
    return jobsList

#view all jobs

def get_all_jobs():
    jobs = Jobs.query.all() 
    jobsList = [job.get_json() for job in jobs]
    return jobsList
