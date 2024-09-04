# School Database Management

This project is a simple Python application that manages a school database using SQLite. The database includes two tables: `students` and `exams`. The application provides a menu-driven interface to perform various operations on these tables, such as adding, updating, deleting, and presenting students and their exams.

## Table of Contents
- [Requirements](#requirements)
- [Database Structure](#database-structure)
- [Features](#features)
- [Usage](#usage)
- [Example Usage](#example-usage)
- [License](#license)

## Requirements

- Python 3.x
- SQLite (comes pre-installed with Python)

## Database Structure

The application manages two tables: `students` and `exams`.

- **students**:
  - `id`: INTEGER, Primary Key
  - `name`: TEXT, Not Null

- **exams**:
  - `id`: INTEGER, Primary Key, AUTOINCREMENT
  - `student_id`: INTEGER, Foreign Key referencing `students(id)` with ON DELETE CASCADE
  - `subject`: TEXT, Not Null
  - `grade`: REAL

## Features

- **Present all students**: Lists all students in the database.
- **Filter exams by student ID**: Lists all exams for a specific student.
- **Add a student**: Inserts a new student into the database.
- **Add an exam**: Inserts a new exam for a student, provided the student exists.
- **Delete an exam**: Removes an exam from the database.
- **Delete a student**: Removes a student and all related exams from the database.
- **Update a student**: Modifies a student's name.
- **Update an exam**: Modifies the subject and grade of an exam.
- **Present all exams**: Lists all exams in the database.

## Usage

1. Clone or download the repository.
2. Run the script:
   ```bash
   python <script_name>.py
