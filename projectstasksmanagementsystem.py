import sqlite3

def create_team_member():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS team_members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_name TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def create_project():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL UNIQUE
    )
    ''')
    conn.commit()
    conn.close()

def create_project_members():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS project_members (
        project_id INTEGER,
        member_name TEXT,
        FOREIGN KEY (project_id) REFERENCES projects (project_id),
        FOREIGN KEY (member_name) REFERENCES team_members (member_name),
        PRIMARY KEY (project_id, member_name)
    )
    ''')
    conn.commit()
    conn.close()

def create_task():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        member_name TEXT NOT NULL,
        task_describe TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (project_id)
    )
    ''')
    conn.commit()
    conn.close()

def add_team_member(member_name):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO team_members (member_name) VALUES (?)', (member_name,))
    conn.commit()
    conn.close()
    print(f"Member {member_name} added successfully.")

def add_project(project_name, member_name):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO projects (project_name) VALUES (?)', (project_name,))
    
    # Get the project ID
    cursor.execute('SELECT project_id FROM projects WHERE project_name = ?', (project_name,))
    project_id = cursor.fetchone()[0]

    cursor.execute('INSERT INTO project_members (project_id, member_name) VALUES (?, ?)', (project_id, member_name))
    conn.commit()
    conn.close()
    print(f"Project '{project_name}' with member '{member_name}' added successfully.")

def add_task(project_name, member_name, task_describe):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT project_id FROM projects WHERE project_name = ?', (project_name,))
    project_id = cursor.fetchone()[0]
    
    cursor.execute('INSERT INTO tasks (project_id, member_name, task_describe) VALUES (?, ?, ?)', (project_id, member_name, task_describe))
    conn.commit()
    conn.close()
    print(f"Task '{task_describe}' added successfully.")

def view_team_member():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM team_members')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"Member ID: {row[0]}, Member Name: {row[1]}")
    else:
        print("No members found.")

def view_project():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT p.project_id, p.project_name, tm.member_name 
    FROM projects p
    LEFT JOIN project_members pm ON p.project_id = pm.project_id
    LEFT JOIN team_members tm ON pm.member_name = tm.member_name
    ''')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"Project ID: {row[0]}, Project Name: {row[1]}, Member Name: {row[2]}")
    else:
        print("No projects found.")

def view_task():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT task_id, p.project_name, member_name, task_describe
    FROM tasks t
    JOIN projects p ON t.project_id = p.project_id
    ''')
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"Task ID: {row[0]}, Project Name: {row[1]}, Member Name: {row[2]}, Task Description: {row[3]}")
    else:
        print("No tasks found.")

def main():
    # Create tables if they don't exist
    create_team_member()
    create_project()
    create_project_members()
    create_task()

    while True:
        print("\n1. Add team member")
        print("2. View team members")
        print("3. Add project")
        print("4. View projects")
        print("5. Add task")
        print("6. View tasks")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            member_name = input("Enter member name: ")
            add_team_member(member_name)

        elif choice == '2':
            view_team_member()

        elif choice == '3':
            project_name = input("Enter project name: ")
            member_name = input("Enter member name associated with this project: ")
            add_project(project_name, member_name)

        elif choice == '4':
            view_project()

        elif choice == '5':
            project_name = input("Enter project name: ")
            member_name = input("Enter member name: ")
            task_describe = input("Enter task description: ")
            add_task(project_name, member_name, task_describe)

        elif choice == '6':
            view_task()

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    