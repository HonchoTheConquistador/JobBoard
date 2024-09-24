import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.models import models
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )
from App.controllers import (
    create_admin, sign_up_applicant, apply_to_job, create_job, 
    get_all_applicants, get_all_applicants_by_jobID, get_jobs_by_company,
    get_all_jobs, view_all_admins, view_all_members)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    initialize2() 
    print('database intialized')

# '''
# User Commands
# '''

# # Commands can be organized using groups

# # create a group, it would be the first argument of the comand
# # eg : flask user <command>
# user_cli = AppGroup('user', help='User object commands') 

# # Then define the command and any parameters and annotate it with the group (@)
# @user_cli.command("create", help="Creates a user")
# @click.argument("username", default="rob")
# @click.argument("password", default="robpass")
# def create_user_command(username, password):
#     create_user(username, password)
#     print(f'{username} created!')

# # this command will be : flask user create bob bobpass

# @user_cli.command("list", help="Lists users in the database")
# @click.argument("format", default="string")
# def list_user_command(format):
#     if format == 'string':
#         print(get_all_users())
#     else:
#         print(get_all_users_json())

# app.cli.add_command(user_cli) # add the group to the cli

# '''
# Test Commands
# '''

# test = AppGroup('test', help='Testing commands') 

# @test.command("user", help="Run User tests")
# @click.argument("type", default="all")
# def user_tests_command(type):
#     if type == "unit":
#         sys.exit(pytest.main(["-k", "UserUnitTests"]))
#     elif type == "int":
#         sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
#     else:
#         sys.exit(pytest.main(["-k", "App"]))
    

# app.cli.add_command(test)


'''
Job Board Commands
'''

jobBoard = AppGroup('job',help="Job Board Commands")

@jobBoard.command("create_admin", help="Adds a new admin to the database")
@click.argument("fname", default="")
@click.argument("lname", default="")
def create_admin_command(fname,lname):
    create_admin(fname,lname)
    print(f'Admin {fname} added!!!')


@jobBoard.command("newapp", help="Adds a new applicant to the database")
@click.argument("fname", default="string")
@click.argument("lname", default="string")
@click.argument("username", default="string")
@click.argument("password", default="string")
def sign_up_applicant_command(fname,lname,username,password):
    sign_up_applicant(fname,lname,username,password)
    print(f'{fname} {lname} registered!!!')

@jobBoard.command("companyjobs", help="Displays all jobs offered by a company")
@click.argument("company", default="string")
def get_jobs_by_company_command(company):
    jobList = get_jobs_by_company(company)
    if not jobList:
        return
    print(f'Jobs offered by {company}:')
    if len(jobList) ==0: print("No Jobs Available...")
    for job in jobList:
        print(job['jobTitle'])

@jobBoard.command("alljobs", help="Displays all jobs offered")
def display_all_jobs():
    jobsList = get_all_jobs()
    print("___JOBS OFFERED___")
    if len(jobsList) ==0: print("No Jobs Available...")
    for i in range(len(jobsList)):
        print(f'{i} | {jobsList[i]["jobTitle"]} | Company: {jobsList[i]["company"]}')

@jobBoard.command("view_applicants", help="Displays all applicants")
@click.argument("staffid", default="string")
@click.argument("fname", default="string")
def view_all_applicants_command(staffid,fname):
    appList = get_all_applicants(staffid,fname)
    if not appList:
        return
    print("___APPLICANT LIST___")
    for i in range(len(appList)):
        print(f"{i} | ID: {applicant_info[i]['id']} {applicant_info[i]['name']}")

@jobBoard.command("view_app_by_id", help="Displays all applicants associated with a given job ID")
@click.argument("staffid", default="string")
@click.argument("fname", default="string")
@click.argument("id", default="string")
def view_all_applicants_by_jobID_command(staffid,fname,id):
    jobID = int(id)
    appList = get_all_applicants_by_jobID(staffid,fname,jobID)
    if not appList:
        return
    print("___APPLICANT LIST___")
    for i in range(len(appList)):
        print(f"{i} | ID: {applicant_info[i]['id']} {applicant_info[i]['name']}")

@jobBoard.command("create_job", help="Given an admin ID, company and title, it creates a new job entry")
@click.argument("staffid", default="string")
@click.argument("fname", default="string")
@click.argument("company", default="string")
@click.argument("jobtitle", default="string")
def create_job_command(company,jobtitle, staffid, fname):
    jobInfo = create_job(company,jobtitle, staffid, fname)
    if not jobInfo:
        return
    print("Successfully added a job!")
    print("Job Added:")
    print(f"{jobInfo['company']} - {jobInfo['jobTitle']}")
    

@jobBoard.command("apply_to_job", help="Given an applicant ID and job ID, applies the applicant to a job")
@click.argument("jobid", default="string")
@click.argument("userid", default="string")
def apply_to_job_command(jobid,userid):
    userInfo, jobInfo = apply_to_job(jobid,userid)
    if not userInfo:
        return 
    print(f"{userInfo['fName']} {userInfo['lName']} applied for: {jobInfo['jobTitle']} in the company {jobInfo['company']}!!")
    

@jobBoard.command("view_admins", help="Displays all admins")
def view_all_admins_command():
    view_all_admins()

@jobBoard.command("view_mem", help="Displays all members")
def view_all_members_command():
    view_all_members()


app.cli.add_command(jobBoard)


def initialize2(): # adds data to the database
    # Admin Creation
    create_admin("Emma", "Miller")
    create_admin("Ava", "Miller")
    create_admin("Isabella", "Martinez")
    create_admin("Sophia", "Smith")

    # Applicant Sign-up
    sign_up_applicant("Aiden", "Jones", "ajones51", "kBqJ!g7vs")
    sign_up_applicant("Emma", "Davis", "edavis91", "eF96%9@F")
    sign_up_applicant("Noah", "Davis", "ndavis68", "mcA$SqZlW3sH")
    sign_up_applicant("Sophia", "Brown", "sbrown93", "VR7Vchqa")
    sign_up_applicant("Noah", "Jones", "njones24", "I%RjB$Q1HHGq")
    sign_up_applicant("Olivia", "Smith", "osmith88", "pGtj2LcM")
    sign_up_applicant("Liam", "Martinez", "lmartinez45", "Qq9&!tYa3")
    sign_up_applicant("Mia", "Garcia", "mgarcia19", "hTr8!KqVp")
    sign_up_applicant("Lucas", "Johnson", "ljohnson33", "LpT3@sD7")
    sign_up_applicant("Amelia", "Clark", "aclark76", "OpS7#eLpT")

    # Job Creation
    create_job("BrightTech", "Graphic Designer", 1, "Emma")
    create_job("TechCorp", "Software Developer", 3, "Isabella")
    create_job("TechCorp", "IT Specialist", 4, "Sophia")
    create_job("InnovateLLC", "Business Analyst", 2, "Ava")
    create_job("BrightTech", "IT Specialist", 1, "Emma")
    create_job("InnoSoft", "Data Analyst", 4, "Sophia")
    create_job("DataWorks", "Project Manager", 2, "Ava")
    create_job("FutureNet", "System Administrator", 3, "Isabella")

    # Job Applications (random values are placeholders)
    # Job Applications
    # Job Applications
    apply_to_job(1, 5)
    apply_to_job(2, 6)
    apply_to_job(3, 7)
    apply_to_job(1, 8)
    apply_to_job(7, 9)
    apply_to_job(5, 10)
    apply_to_job(4, 11)
    apply_to_job(6, 12)
    apply_to_job(8, 13)
    apply_to_job(2, 14)
    apply_to_job(3, 9)
    apply_to_job(5, 11)


