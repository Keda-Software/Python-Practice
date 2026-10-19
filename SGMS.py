
# # Student Grade Management System

# name = input("Enter student name: ")

# mark1 = float(input("Enter mark for Python: "))
# mark2 = float(input("Enter mark for Database: "))
# mark3 = float(input("Enter mark for Networking: "))

# # Calculate average
# average = (mark1 + mark2 + mark3) / 3

# # Determine grade
# if average >= 90:
#     grade = "A"
# elif average >= 80:
#     grade = "B"
# elif average >= 70:
#     grade = "C"
# elif average >= 60:
#     grade = "D"
# else:
#     grade = "F"

# # Display result
# print("\n--- Student Result ---")
# print("Name:", name)
# print("Average:", round(average, 2))
# print("Grade:", grade)

# if average >= 50:
#     print("Status: PASS")
# else:
#     print("Status: FAIL")


import json
import os

FILE_NAME = "students.json"


# Load saved students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Get valid marks
def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


# Add a student
def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if any(s["id"].lower() == student_id.lower()
           for s in students):
        print("This student ID already exists!")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    python_mark = get_mark("Python")
    database_mark = get_mark("Database")
    networking_mark = get_mark("Networking")

    average = (python_mark + database_mark + networking_mark) / 3

    student = {
        "id": student_id,
        "name": name,
        "marks": {
            "Python": python_mark,
            "Database": database_mark,
            "Networking": networking_mark
        },
        "average": round(average, 2),
        "grade": calculate_grade(average),
        "status": "PASS" if average >= 50 else "FAIL"
    }

    students.append(student)
    save_students(students)

    print("\nStudent saved successfully!")


# Search for a student by ID or name
def search_student(students):
    keyword = input("Enter student ID or name: ").strip().lower()

    if not keyword:
        print("Please enter an ID or name.")
        return

    results = [
        s for s in students
        if keyword == s["id"].lower()
        or keyword in s["name"].lower()
    ]

    if results:
        for s in results:
            print("\n--- Student Record ---")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            print("Average:", s["average"])
            print("Grade:", s["grade"])
            print("Status:", s["status"])
    else:
        print("Student not found.")


# Display all students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- All Students ---")

    for s in students:
        print(
            f'ID: {s["id"]} | '
            f'Name: {s["name"]} | '
            f'Average: {s["average"]} | '
            f'Grade: {s["grade"]} | '
            f'Status: {s["status"]}'
        )


# Main program
students = load_students()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_student(students)
    elif choice == "2":
        search_student(students)
    elif choice == "3":
        view_students(students)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Choose 1, 2, 3, or 4.")

