import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('task_tracker.db')

# Create a cursor
c = conn.cursor()

# Create a table to store tasks
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    assignee TEXT NOT NULL,
    due_date TEXT,
    status TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

def add_task(task_name, assignee, due_date, status="Not Started"):
    conn = sqlite3.connect('task_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task_name, assignee, due_date, status) VALUES (?, ?, ?, ?)",
              (task_name, assignee, due_date, status))
    conn.commit()
    conn.close()
    print(f"Task '{task_name}' assigned to {assignee} added successfully!")

def view_tasks():
    conn = sqlite3.connect('task_tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(f"ID: {row[0]}, Task: {row[1]}, Assignee: {row[2]}, Due Date: {row[3]}, Status: {row[4]}")

def update_task_status(task_id, new_status):
    conn = sqlite3.connect('task_tracker.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()
    print(f"Task ID {task_id} status updated to '{new_status}'")

def delete_task(task_id):
    conn = sqlite3.connect('task_tracker.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task ID {task_id} deleted.")

def menu():
    print("""
    ==== Task Assignment and Tracking System ====
    1. Add Task
    2. View All Tasks
    3. Update Task Status
    4. Delete Task
    5. Exit
    """)

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            assignee = input("Enter assignee name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(task_name, assignee, due_date)
        
        elif choice == '2':
            view_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (Not Started, In Progress, Completed): ")
            update_task_status(task_id, new_status)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        
        elif choice == '5':
            print("Exiting Task Tracker. Goodbye!")
            break
        
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
