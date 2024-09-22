# from datetime import DateTime
from sqlalchemy.exc import IntegrityError 
from database import SessionLocal,tables
from models.project import Project
from models.task import Task
from models.status import Status
import click

def create_project(name, description):
    """Create a new project."""
    db = SessionLocal() # Start a new database session
    project = Project(name=name, description=description)# Create a new Project instance
    db.add(project) # Add the project to the session
    try:
        db.commit() # Commit the session to save changes
        click.echo(f'Project "{name}" created successfully!')
    except IntegrityError:
        db.rollback()# Rollback changes if there is an error
        click.echo("Error: Project with this name already exists.")
    finally:
        db.close()# close the session

def delete_project(project_id):
    """Delete a project by its ID."""
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()# Retrieve the project
    if project:
        db.delete(project)# Delete the project from the session
        db.commit()# Commit the changes
        click.echo(f'Project {project_id} deleted.')
    else:
        click.echo('Error: Project not found.')
    db.close()

def add_task(project_id, title, description, due_date):
    """Add a task to a project."""
    db = SessionLocal()
    task = Task(title=title, description=description, due_date=due_date, project_id=project_id)# Create a task instance
    db.add(task)# Add the task to the session
    try:
        db.commit() # Commit the session
        click.echo(f'Task "{title}" added to project {project_id}.')
    except IntegrityError:
        db.rollback()# Rollback if an error occurs
        click.echo("Error: Could not add task to project.")
    finally:
        db.close()

def complete_task(task_id):
    """Mark a task as completed."""
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first() # Retrieve the task
    if task:
        task.status = Status.COMPLETED # Update the task status to completed
        db.commit()# Commit the changes
        click.echo(f'Task {task_id} marked as completed.')
    else:
        click.echo('Error: Task not found.')
    db.close()

def delete_task(task_id):
    """Delete a task."""
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()# Retrieve the task
    if task:
        db.delete(task)# Delete the task from the session
        db.commit()# Commit the changes
        click.echo(f'Task {task_id} deleted.')
    else:
        click.echo('Error: Task not found.')
    db.close()

def list_tasks(project_id):
    """List all tasks for a specific project by its ID."""
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()# Retrieve Project 
    
    if project:
        tasks = project.tasks#A ccess the project tasks
        if tasks:
            click.echo(f'Tasks for Project ID {project_id} - {project.name}:')
            for task in tasks:
                click.echo(f'Task ID: {task.id}, Title: {task.title}, Status: {task.status}, Due Date: {task.due_date}')
        else:
            click.echo(f'No tasks found for Project ID {project_id}.')
    else:
        click.echo('Error: Project not found.')
    db.close()

def list_projects():
    """List all projects."""
    db = SessionLocal()
    projects = db.query(Project).all() #Retrieve all the projects
    if projects:
        for project in projects:
            click.echo(f'Project ID: {project.id}, Name: {project.name}, Description: {project.description}')
    else:
        click.echo('No projects found.')
    db.close()

def find_tasks_by_status(status):
    """Find tasks by status (pending/completed)."""
    db = SessionLocal()
    tasks = db.query(Task).filter(Task.status == Status[status.upper()]).all() # Filter tasks by status
    if tasks:
        for task in tasks:
            click.echo(f'Task ID: {task.id}, Title: {task.title}, Due Date: {task.due_date}')
    else:
        click.echo('No tasks found for this status.')
    db.close()

def main_menu():
    """Display the main menu and handle user input."""
    while True:
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
        
        choice = click.prompt("Select an option", type=int)

        if choice == 1:
            name = click.prompt("Enter project name")
            description = click.prompt("Enter project description")
            create_project(name, description)# Call the function to create a project
        
        elif choice == 2:
            project_id = click.prompt("Enter project ID", type=int)
            delete_project(project_id)# Call the function to delete a project
        
        elif choice == 3:
            project_id = click.prompt("Enter project ID", type=int)
            title = click.prompt("Enter task title")
            description = click.prompt("Enter task description", default="")
            due_date = click.prompt("Enter due date (YYYY-MM-DD HH:MM:SS)", default=None, type=click.DateTime(formats=["%Y-%m-%d %H:%M:%S"]))
            add_task(project_id, title, description, due_date)# Call the function to add a task

        elif choice == 4:
            task_id = click.prompt("Enter task ID", type=int)
            complete_task(task_id)# Call the function to mark a task as completed

        elif choice == 5:
            task_id = click.prompt("Enter task ID", type=int)
            delete_task(task_id)# Call the function to delete a task

        elif choice == 6:
            list_projects()# Call the function to list all projects

        elif choice == 7:
            status = click.prompt("Enter status (pending/completed)", type=click.Choice(['pending', 'completed'], case_sensitive=False))
            find_tasks_by_status(status)# Call the function to find tasks by status

        elif choice == 8:
            project_id = click.prompt("Enter project ID", type=int)
            list_tasks(project_id)# Call the function to list tasks for a project

        elif choice == 0:
            click.echo("Exiting...")
            break# Exit the menu loop
        
        else:
            click.echo("Invalid option, please try again.")

if __name__ == "__main__":
    tables()  # Ensure database is initialized before using the CLI
    main_menu()# Start the main menu
