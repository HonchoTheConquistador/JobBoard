# COMP 3613 A1 - Job Board 

## Brief Introduction 
This repository houses a code solution for the job board problem.

## Contents

1. Problem Definition
2. Explanation of Solution 
3. Outline of CLI functionality
    a. Prepatory Function
    b. Regular Functions

## Problem Definition 

Currently there is a need for a CLI application to assist with the management of a job board.
The requirements are as follows: 

An app to post job openings and view the applicants
- Create Job
- View Jobs
- Apply to Job
- View Job applicants

## Explanation of Solution 

To alleviate the problems of the user, a CLI application was constructed. Utilising the [flaskmvc](https://github.com/uwidcit/flaskmvc) template, this solution 
implemented the four requirements outlined in the problem definition definition in the python programming language.


## Outline of CLI functionality 

### Prepatory Functions

Before executing the regular functions, the following command must be run:

```bash
$ flask init
```

### Regular Functions
In this project, 10 functions were created to fulfill the needs of the user. Each function starts with the command line prefix:

```bash
$ flask job
```

The available commands are as follows along with their description:

| Command          | Description                                                        |
|------------------|--------------------------------------------------------------------|
| alljobs          | Displays all jobs offered                                          |
| apply_to_job     | Given an applicant ID and job ID, applies the applicant to a job    |
| companyjobs      | Displays all jobs offered by a company                             |
| create_admin     | Adds a new admin to the database                                   |
| create_job       | [ADMIN] Given an admin ID, company and title, it creates a new job entry |
| newapp           | Adds a new applicant to the database                               |
| view_admins      | Displays all admins                                                |
| view_app_by_id   | [ADMIN] Displays all applicants associated with a given job ID     |
| view_applicants  | [ADMIN] Displays all applicants                                    |
| view_mem         | Displays all members                                               |

As an aside, the descriptions which start with [ADMIN] can only be executed when the right staff id and first name combination are entered.


| Command | Description |
| --- | --- |
| `flask job create_admin <fname> <lname>` | Creates a new admin with the given first and last name. |
| `flask job newapp <fname> <lname> <username> <password>` | Creates a new applicant with the given first name, last name, username, and password. |
| `flask job companyjobs <company>` | Displays all the jobs offered by the given company. |
| `flask job alljobs` | Displays all the jobs offered. |
| `flask job view_applicants <staffid> <fname>` | Displays all the applicants for the admin with the given staff ID and first name. |
| `flask job view_app_by_id <staffid> <fname> <id>` | Displays all the applicants associated with the job with the given ID, for the admin with the given staff ID and first name. |
| `flask job create_job <staffid> <fname> <company> <jobtitle>` | Creates a new job with the given job title at the given company, for the admin with the given staff ID and first name. |
| `flask job apply_to_job <jobid> <userid>` | Applies the user with the given ID to the job with the given ID. |
| `flask job view_admins` | Displays all the admins. |
| `flask job view_mem` | Displays all the members. |


#### Usage

```bash
flask job create_job 1 Emma BrightTech "Graphic Designer"
```
This command creates a new job with the job title "Graphic Designer" at the company "BrightTech", with the admin user "Emma" (staff ID 1).
---

```bash
flask job apply_to_job 1 5
```
This command applies the user with ID 5 (Aiden Jones) to the job with ID 1 (Graphic Designer at BrightTech).


```bash
flask job view_app_by_id 1 Emma 1
```
This command displays all the applicants associated with the job with ID 1 (Graphic Designer at BrightTech), for the admin user "Emma" (staff ID 1).


```bash
flask job newapp "Ethan" "Wilson" "ewilson23" "password123"
```
This command creates a new applicant with the first name "Ethan", last name "Wilson", username "ewilson23", and password "password123".


```bash
flask job view_applicants 2 Ava
```
This command displays all the applicants for the admin user "Ava" (staff ID 2).


```bash
flask job companyjobs "TechCorp"
```
This command displays all the jobs offered by the company "TechCorp".


```bash
flask job alljobs
```
This command displays all the jobs offered.


```bash
flask job create_admin "Emma" "Miller"
```
This command creates a new admin with the first name "Emma" and last name "Miller".


```bash
flask job view_admins
```
This command displays all the admins.


```bash
flask job view_mem
```
This command displays all the members.