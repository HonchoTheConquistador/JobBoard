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

#view jobs by company 
def get_jobs_by_company(companyName):
    companyOfferings = Jobs.query.filter_by(company=companyName)
    if not company:
        print("Error finding company!!!")
        return None
    jobsList = [job.get_json() for job in companyOfferings]
    return jobsList

#view all jobs

def get_all_jobs():
    jobs = Jobs.query.all() 
    jobsList = [job.get_json() for job in jobs]
    return jobsList



#view applicants -----------admin-------------

def get_all_applicants(staffID, fName):
    jobsList = JobApplications.query.all()
    findAdmin = Admin.query.filter_by(staffID=staffID,fName=fName).first()
    if not findAdmin:
        print("Error!!!")
        return None
    jobApplications = JobApplications.query.all()
    if not jobApplications:
        print(f"No applicants found!!!")
        return

    print(f"All Job Applicants:")
    for application in jobApplications:
        # Get the applicant information
        applicant = Applicant.query.get(application.userID)
        if applicant:
            applicant_info = {
                'id': applicant.id,
                'name': f"{applicant.fName} {applicant.lName}"
            }
            applicants_list.append(applicant_info)
        else:
            print(f"- Unknown applicant (ID: {application.userID})")

    return applicants_list

#view applicants by job id -----------admin--------
def get_all_applicants_by_jobID(staffID, fName, id):
    # Verify admin
    findAdmin = Admin.query.filter_by(staffID=staffID, fName=fName).first()
    if not findAdmin:
        print("Error: Invalid admin credentials")
        return None

    # Get all job applications for the given job ID
    jobApplications = JobApplications.query.filter_by(jobID=id).all()
    if not jobApplications:
        print(f"No applicants found for job ID: {id}")
        return None

    applicants_list = []

    print(f"Applicants for job ID {id}:")
    for application in jobApplications:
        # Get the applicant information
        applicant = Applicant.query.get(application.userID)
        if applicant:
            applicant_info = {
                'id': applicant.id,
                'name': f"{applicant.fName} {applicant.lName}"
            }
            applicants_list.append(applicant_info)
            
        else:
            print(f"- Unknown applicant (ID: {application.userID})")

    return applicants_list

#create Job ------------------------------admin-------------

def create_job(company,jobTitle, staffID, fName):
    job = Jobs(company, jobTitle)
    findAdmin = Admin.query.filter_by(staffID=staffID,fName=fName).first()
    jobCheck = Jobs.query.filter_by(company=company,jobTitle=jobTitle).first()
    if jobCheck:
        print("Job already exists!!!")
        return
    if not findAdmin:
        print("Not a valid administrator!!!")
        return
    print("Successfully added a job!")
    db.session.add(job)
    db.session.commit()
    return

#apply to job 

def apply_to_job(jobID,userID):
    job = Jobs.query.filter_by(jobID=jobID).first()
    user = Applicant.query.filter_by(id=userID).first()
    if not job or not user:
        print("Error applying to job!!!")
    allJobs = JobApplications.query.filter_by(jobID=jobID,userID=userID).first()
    newJobApplication = JobApplications(jobID,userID)
    if allJobs: #checks to see if the job application exists already
        print("Job application already exists!!!")
        return
    db.session.add(newJobApplication)
    db.session.commit()
    return
