TASK ASSIGNMENT AND TRACKING SYSTEM

OVERVIEW
This project is a command-line based Task Assignment and Tracking System developed using Python and SQLite.
It helps users create, assign, track, update, and delete tasks efficiently using a local database.
The system is suitable for managing tasks within small teams or for personal task tracking.

OBJECTIVE
The objective of this project is to provide a simple and effective way to assign tasks, track their progress, and manage task status using a lightweight database.

FEATURES

• Add new tasks with assignee and due date
• View all tasks with detailed information
• Update task status (Not Started, In Progress, Completed)
• Delete tasks using task ID
• Persistent storage using SQLite database

TECHNOLOGIES USED

• Programming Language: Python 3
• Database: SQLite (sqlite3 module)

PROJECT FILES

• task_tracker.py – Main Python application file
• task_tracker.db – SQLite database file (automatically created)

DATABASE STRUCTURE

Table Name: tasks

Fields:
• id – Unique task ID (Auto Increment)
• task_name – Name/description of the task
• assignee – Person responsible for the task
• due_date – Task due date
• status – Task status (Not Started, In Progress, Completed)

HOW THE SYSTEM WORKS

The program connects to a SQLite database or creates one if it does not exist

A tasks table is created automatically

User interacts with the system through a menu-driven interface

Based on user input, tasks are added, viewed, updated, or deleted

All task data is stored permanently in the database

MENU OPTIONS

Add Task

View All Tasks

Update Task Status

Delete Task

Exit

HOW TO RUN THE PROJECT

Step 1: Ensure Python 3 is installed on your system
Step 2: Save the Python file as task_tracker.py
Step 3: Open terminal or command prompt
Step 4: Navigate to the project directory
Step 5: Run the program using the command

python task_tracker.py

SECURITY AND BEST PRACTICES

• Uses parameterized SQL queries to prevent SQL injection
• Ensures proper database connection handling
• Uses auto-increment IDs to uniquely identify tasks

PROJECT USE CASES

This project can be used for:
• College Mini Project
• Python Practice Project
• Task Management System
• Resume Project for Entry-Level Roles

FUTURE ENHANCEMENTS

• Add user authentication
• Filter tasks by status or assignee
• Export tasks to Excel or CSV
• Add reminders for due dates
• Convert to a web application using Flask or Django

AUTHOR

Developed by: Yash Raj
