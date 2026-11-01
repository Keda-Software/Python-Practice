
# STUDENT INFORMATION SYSTEM

print("===== STUDENT REGISTRATION =====")

name = input("Enter student name: ")
student_id = int(input("Enter student ID: "))
age = int(input("Enter student age: "))
department = input("Enter department: ")

# Store grades in a list
grades = []

subject1 = float(input("Enter Python grade: "))
subject2 = float(input("Enter Database grade: "))
subject3 = float(input("Enter HTML grade: "))

grades.append(subject1)
grades.append(subject2)
grades.append(subject3)

# Calculate total and average
total = sum(grades)
average = total / len(grades)

# Determine result
passed = average >= 50

# Store student information
student = {
    "name": name,
    "id": student_id,
    "age": age,
    "department": department,
    "grades": grades,
    "total": total,
    "average": average,
    "passed": passed
}

# Display result
print("\n================================")
print("       STUDENT REPORT")
print("================================")

print("Name:", student["name"])
print("Student ID:", student["id"])
print("Age:", student["age"])
print("Department:", student["department"])

print("--------------------------------")
print("Python:", student["grades"][0])
print("Database:", student["grades"][1])
print("HTML:", student["grades"][2])

print("--------------------------------")
print("Total:", student["total"])
print("Average:", student["average"])
print("Result:", "PASS" if passed else "FAIL")

print("================================")
