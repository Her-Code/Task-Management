# Task Management System

## Overview
This is a command-line based Task Management System built with Python, SQLAlchemy, and SQLite. It allows users to create projects, manage tasks, and track their statuses through a simple CLI interface.

## Features
- create and delete projects
- Add,complete and delete tasks
- List all projects and tasks
- Filter tasks by status(pending/completed)

## Requirements
- Python 3 version
- SQLAlchemy
- SQLite(include Python)

## Installation

1. `pip install SQLAlchemy`
   `pip install alembic`
    `pip install click`
    `pipenv install`
2. mkdir TASK_MANAGEMENT
  - cd Task_Management
  - git add .
  - git commit -m ""
  - git push origin main

3. Initialize the database and create tables
  - python runfile.py

4. Follow the prompts in the menu to manage your projects and tasks.

## Commands
1. Create Project
2. Delete Project
3. Add Task
4. Complete Task
5. Delete Task
6. List Projects
7. Find Tasks by Status
8. List Tasks for a Project
0. Exit

## Structure
1. database.py:Database connection and session management.
   ` db_URL = "sqlite:///tasks.db" `
2. models/project.py:Contains model definitions for Project, Task, and Status.
   ` __tablename__= 'projects'`
3. models/status.py: Contains model definitions for Task
   ` PENDING = "pending"
    COMPLETED = "completed" `
4. models/task.py: Contains model definitions for Status
   `  __tablename__='tasks' `
5. runfile.py:Contains the main logic and CLI interface.
  ` while True:
        click.echo("\n--- Task Management System Menu ---")
        click.echo("1. Create Project")
        click.echo("2. Delete Project")
        click.echo("3. Add Task")
        click.echo("4. Complete Task")
        click.echo("5. Delete Task")
        click.echo("6. List Projects")
        click.echo("7. Find Tasks by Status")
        click.echo("8. List Tasks for a Project")
        click.echo("0. Exit")
        
        choice = click.prompt("Select an option", type=int) `

## Author
[Her-Code](https://github.com/Her-Code) - Sharon Kahira
