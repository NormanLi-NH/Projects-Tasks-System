# Project Management System
This Python script implements a simple project management system using SQLite as the database. It allows users to manage team members, projects, and tasks efficiently.

### Features
- Create and manage team members
- Create and manage projects
- Assign team members to projects
- Create and manage tasks associated with projects
- View team members, projects, and tasks
### Requirements
- Python 3.x
- SQLite (comes built-in with Python)
### Setup

1. Clone the repository (if applicable):
```bash
git clone <repository-url>
cd <repository-directory>
Run the script:
```

2. Run the script:
```bash
python project_management.py
```

# Functions
### Database Initialization
- create_team_member(): Creates a table for team members.
- create_project(): Creates a table for projects.
- create_project_members(): Creates a table to link projects and team members.
- create_task(): Creates a table for tasks.

### Data Management

- add_team_member(member_name): Adds a new team member.
- add_project(project_name, member_name): Adds a new project and assigns a member.
- add_task(project_name, member_name, task_describe): Adds a new task to a project.

### Data Viewing

- view_team_member(): Displays all team members.
- view_project(): Displays all projects with associated members.
- view_task(): Displays all tasks with their associated projects.

### Usage

1. Upon running the script, you will be presented with a menu:
- Add team member
- View team members
- Add project
- View projects
- Add task
- View tasks
- Exit

2. Follow the prompts to manage your projects and tasks.

### Example

To add a team member:

- Select option 1
- Enter the member name when prompted.

To view all team members:

- Select option 2.

### Notes
- Ensure you have write permissions for the directory where the database file my_database.db will be created.
- The database will be created in the same directory as the script if it does not already exist.

### License
This project is open-source and available under the MIT License. Feel free to contribute!