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

Here’s the table without the backticks:

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

As an aside, the descriptions which start with [ADMIN] can only be executed when the right staff id and first name combination are entered