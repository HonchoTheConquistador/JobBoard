from App.models.models import *
from App.database import db

#create admin 

def create_admin(fName,lName):
    newAdmin = Admin(fName,lName)
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
    if not companyOfferings:
        
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
    findAdmin = Admin.query.filter_by(id=staffID,fName=fName).first()
    if not findAdmin:
        print("Error, not an administrator!!!")
        return None
    jobApplications = JobApplications.query.all()
    if not jobApplications:
        print(f"No applicants found!!!")
        return None
    applicants_list = []
    for application in jobApplications:
        # Get the applicant information
        applicant = Applicant.query.get(application.userID)
        job = Jobs.query.get(application.jobID)
        if applicant:
            if job:
                applicant_info = {
                    'id': applicant.id,
                    'name': f"{applicant.fName} {applicant.lName}",
                    'company': f"{job.company}",
                    'jobTitle': f"{job.jobTitle}"
                }
            else:
                print("Error in both Applicant and Job!!!")
                return None
            applicants_list.append(applicant_info)
        else:
            print(f"- Unknown applicant (ID: {application.userID})")
            return None 

    return applicants_list

#view applicants by job id -----------admin--------
def get_all_applicants_by_jobID(staffID, fName, id):
    # Verify admin
    findAdmin = Admin.query.filter_by(id=staffID, fName=fName).first()
    if not findAdmin:
        print("Error: Invalid admin credentials")
        return None, None

    # Get all job applications for the given job ID
    jobApplications = JobApplications.query.filter_by(jobID=id).all()
    if not jobApplications:
        print(f"No applicants found for job ID: {id}")
        return None, None

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
    job = Jobs.query.get(id)
    job_info = job.get_json()
    return applicants_list, job_info

#create Job ------------------------------admin-------------

def create_job(company,jobTitle, staffID, fName):
    
    findAdmin = Admin.query.filter_by(id=staffID,fName=fName).first()
    jobCheck = Jobs.query.filter_by(company=company,jobTitle=jobTitle).first()
    if jobCheck: #checks if job exists
        print("Job already exists!!!")
        return None
    if not findAdmin:
        print("Not a valid administrator!!!")
        return None
    job = Jobs(company, jobTitle)
    db.session.add(job)
    db.session.commit()
    jobInfo = job.get_json()
    return jobInfo

#apply to job 

def apply_to_job(jobID,userID):
    job = Jobs.query.filter_by(id=jobID).first()
    user = Applicant.query.filter_by(id=userID).first()
    if not job: # Job does not exist  
        print("Job does not exist!!!")
        return None, None
    if not user:
        print("Error: User was not able to be apply!!")
        return None,None
    allJobs = JobApplications.query.filter_by(jobID=jobID,userID=userID).first()
    newJobApplication = JobApplications(jobID,userID)
    if allJobs: #checks to see if the job application exists already
        print("Job application already exists!!!")
        return None, None 
    db.session.add(newJobApplication)
    db.session.commit()
    userInfo = user.get_json()
    jobInfo = job.get_json()
    return userInfo, jobInfo

def view_all_admins():
    admins = Admin.query.all()
    if not admins:
        print("No admins available!!!")
        return 
    for admin in admins:
        print(f"{admin.id} - {admin.fName} {admin.lName}")

def view_all_members(): #views all registered members, applicant or not
    apps = Applicant.query.all()
    if not apps:
        print("No applicants available!!!")
        return 
    for app in apps:
        print(f"{app.id} - {app.fName} {app.lName}")