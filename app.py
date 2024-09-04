import sqlite3

# Initialize the database connection
conn = sqlite3.connect('school.db')
c = conn.cursor()

# Create the tables if they don't exist
c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade REAL,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
)
''')

conn.commit()

# Function to present all students
def present_students():
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

# Function to filter exams by student ID
def filter_exams_by_student_id(student_id):
    c.execute('SELECT * FROM exams WHERE student_id = ?', (student_id,))
    exams = c.fetchall()
    for exam in exams:
        print(f"Exam id:{exam[0]}, Subject: {exam[2]}, Grade: {exam[3]}")

# Function to add a student
def add_student(name):
    c.execute('INSERT INTO students (name) VALUES (?)', (name,))
    conn.commit()

# Function to add an exam (only if the student exists)
def add_exam(student_id, subject, grade):
    c.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    if c.fetchone():
        c.execute('INSERT INTO exams (student_id, subject, grade) VALUES (?, ?, ?)', (student_id, subject, grade))
        conn.commit()
    else:
        print("Student does not exist. Cannot add exam.")

# Function to delete an exam
def delete_exam(exam_id):
    c.execute('DELETE FROM exams WHERE id = ?', (exam_id,))
    conn.commit()

# Function to delete a student (and related exams)
def delete_student(student_id):
    c.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()

# Function to update a student
def update_student(student_id, new_name):
    c.execute('UPDATE students SET name = ? WHERE id = ?', (new_name, student_id))
    conn.commit()

# Function to update an exam
def update_exam(exam_id, new_subject, new_grade):
    c.execute('UPDATE exams SET subject = ?, grade = ? WHERE id = ?', (new_subject, new_grade, exam_id))
    conn.commit()

# Function to present all exams
def present_all_exams():
    c.execute('SELECT * FROM exams')
    exams = c.fetchall()
    for exam in exams:
        print(f"Student ID: {exam[1]}, Subject: {exam[2]}, Grade: {exam[3]}")

# Menu function
def menu():
    while True:
        print("\nMenu:")
        print("1. Present all students")
        print("2. Filter exams by student ID")
        print("3. Add a student")
        print("4. Add an exam")
        print("5. Delete an exam")
        print("6. Delete a student")
        print("7. Update a student")
        print("8. Update an exam")
        print("9. Present all exams")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            present_students()
        elif choice == '2':
            student_id = input("Enter student ID: ")
            filter_exams_by_student_id(student_id)
        elif choice == '3':
            name = input("Enter student name: ")
            add_student(name)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            add_exam(student_id, subject, grade)
        elif choice == '5':
            exam_id = input("Enter exam ID: ")
            delete_exam(exam_id)
        elif choice == '6':
            student_id = input("Enter student ID: ")
            delete_student(student_id)
        elif choice == '7':
            student_id = input("Enter student ID: ")
            new_name = input("Enter new name: ")
            update_student(student_id, new_name)
        elif choice == '8':
            exam_id = input("Enter exam ID: ")
            new_subject = input("Enter new subject: ")
            new_grade = float(input("Enter new grade: "))
            update_exam(exam_id, new_subject, new_grade)
        elif choice == '9':
            present_all_exams()
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    menu()

# Close the connection when done
conn.close()
