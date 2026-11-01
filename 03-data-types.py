
# ==========================================
# PYTHON COURSE - TOPIC 03
# PYTHON DATA TYPES
# ==========================================

# 1. STRING DATA TYPE (str)

student_name = "Abebe"
country = "Ethiopia"
department = "Software Engineering"

print("STUDENT INFORMATION")
print(student_name)
print(country)
print(department)

print(type(student_name))
print(type(country))

# 2. INTEGER DATA TYPE (int)

age = 22
year = 2026
student_id = 1001

print("\nINTEGER EXAMPLES")
print(age)
print(year)
print(student_id)

print(type(age))

# 3. FLOAT DATA TYPE (float)

price = 150.50
salary = 25000.75
average = 89.5

print("\nFLOAT EXAMPLES")
print(price)
print(salary)
print(average)

print(type(price))

# 4. BOOLEAN DATA TYPE (bool)

is_student = True
is_employed = False
is_registered = True

print("\nBOOLEAN EXAMPLES")
print(is_student)
print(is_employed)
print(is_registered)

print(type(is_student))

# 5. LIST DATA TYPE (list)

students = ["Abebe", "Kebede", "Marta", "Hana"]

print("\nLIST EXAMPLES")
print(students)
print(students[0])
print(students[1])

# Adding an item
students.append("Dawit")
print(students)

# Removing an item
students.remove("Kebede")
print(students)

print(type(students))

# 6. TUPLE DATA TYPE (tuple)

colors = ("Red", "Green", "Blue")

print("\nTUPLE EXAMPLES")
print(colors)
print(colors[0])
print(colors[1])

print(type(colors))

# 7. SET DATA TYPE (set)

numbers = {10, 20, 30, 40, 10}

print("\nSET EXAMPLES")
print(numbers)

# Adding a value
numbers.add(50)
print(numbers)

# Removing a value
numbers.remove(20)
print(numbers)

print(type(numbers))

# 8. DICTIONARY DATA TYPE (dict)

student = {
    "name": "Abebe",
    "age": 22,
    "city": "Dessie",
    "grade": 89.5
}

print("\nDICTIONARY EXAMPLES")
print(student)

print(student["name"])
print(student["age"])
print(student["city"])

# Updating dictionary
student["grade"] = 95
print(student)

# Adding new information
student["department"] = "Software Engineering"
print(student)

print(type(student))

# 9. CHECK MULTIPLE DATA TYPES

data1 = "Python"
data2 = 100
data3 = 25.5
data4 = True
data5 = [1, 2, 3]

print("\nCHECK DATA TYPES")
print(type(data1))
print(type(data2))
print(type(data3))
print(type(data4))
print(type(data5))

# 10. REAL WORLD STUDENT RECORD

name = input("\nEnter student name: ")
age = int(input("Enter student age: "))
grade = float(input("Enter student grade: "))

passed = grade >= 50

student_record = {
    "name": name,
    "age": age,
    "grade": grade,
    "passed": passed
}

print("\n========== STUDENT RECORD ==========")
print("Name:", student_record["name"])
print("Age:", student_record["age"])
print("Grade:", student_record["grade"])
print("Passed:", student_record["passed"])
print("====================================")

# END OF TOPIC 03
