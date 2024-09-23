import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )
from App.controllers import (
    create_admin, sign_up_applicant, apply_to_job, create_job, 
    get_all_applicants, get_all_applicants_by_jobID, get_jobs_by_company,
    get_all_jobs)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)


'''
Job Board Commands
'''

jobBoard = AppGroup('job',help="Job Board Commands")

@jobBoard.command("create_admin", help="Adds a new admin to the database")
@click.argument("fName", default="string")
@click.argument("lName", default="string")
def create_admin_command(fName,lName):
    create_admin(fName,lName)
    print(f'Admin {fName} added!!!')


@jobBoard.command("newapp", help="Adds a new applicant to the database")
@click.argument("fName", default="string")
@click.argument("lName", default="string")
@click.argument("username", default="string")
@click.argument("password", default="string")
def sign_up_applicant_command(fName,lName,username,password):
    sign_up_applicant(fName,lName,username,password)
    print(f'{fName} {lName} registered!!!')

@jobBoard.command("companyjobs", help="Displays all jobs offered by a company")
@click.argument("company", default="string")
def get_jobs_by_company_command(company):
    jobList = get_jobs_by_company(company)
    if not jobList:
        return
    print(f'Jobs offered by {company}:')
    for job in jobList:
        print(job['jobTitle'])

@jobBoard.command("alljobs", help="Displays all jobs offered")
def display_all_jobs():
    jobsList = get_all_jobs()
    print("___JOBS OFFERED___")
    for i in range(len(jobsList)):
        print(f'{i} | {jobsList[i]["JobTitle"]} | Company: {jobsList[i]["company"]}')

@jobBoard.command("view_applicants", help="Displays all applicants")
@click.argument("staffID", default="string")
@click.argument("fName", default="string")
def view_all_applicants_command(staffID,fName):
    appList = get_all_applicants(staffID,fName)
    if not appList:
        return
    print("___APPLICANT LIST___")
    for i in range(len(appList)):
        print(f"{i} | ID: {applicant_info[i]['id']} {applicant_info[i]['name']}")

@jobBoard.command("view_app_by_id", help="Displays all applicants when given a job ID")
@click.argument("staffID", default="string")
@click.argument("fName", default="string")
@click.argument("id", default="string")
def view_all_applicants_by_jobID_command(staffID,fName,id):
    jobID = int(id)
    appList = get_all_applicants_by_jobID(staffID,fName,jobID)
    if not appList:
        return
    print("___APPLICANT LIST___")
    for i in range(len(appList)):
        print(f"{i} | ID: {applicant_info[i]['id']} {applicant_info[i]['name']}")







app.cli.add_command(jobBoard)