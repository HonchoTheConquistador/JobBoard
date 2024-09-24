# COMP 3613 A1 - Job Board 

## Brief Introduction 
This repository houses a code solution for the job board problem.

## Contents

1. Problem Definition
2. Explanation of Solution 
3. Outline of CLI functionality

## Problem Definition 

Currently there is a need for a CLI application to assist with the management of a job board.
The requirements are as follows: 

An app to post job openings and view the applicants
•	Create Job
•	View Jobs
•	Apply to Job
•	View Job applicants

## Explanation of Solution 

To alleviate the problems of the user, a CLI application was constructed. Utilising the [flaskmvc](https://github.com/uwidcit/flaskmvc) template, this solution 
implemented the four requirements outlined in the problem definition definition in the python programming language.


## Outline of CLI functionality 


```bash
$ flask init
```

```python
# inside wsgi.py

user_cli = AppGroup('user', help='User object commands')

@user_cli.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

app.cli.add_command(user_cli) # add the group to the cli

```