
# ==========================================
# PYTHON COURSE - TOPIC 02
# VARIABLES AND NAMING RULES
# ==========================================

# 1. Creating Variables
name = "Abebe"
age = 22
city = "Dessie"
country = "Ethiopia"

print(name)
print(age)
print(city)
print(country)

# 2. Different Variable Types
student_name = "Kebede"
student_age = 21
student_grade = 89.5
is_student = True

print(student_name)
print(student_age)
print(student_grade)
print(is_student)

# 3. Checking Variable Types
print(type(student_name))
print(type(student_age))
print(type(student_grade))
print(type(is_student))

# 4. Updating Variables
price = 100
print("Old Price:", price)

price = 200
print("New Price:", price)

# 5. Assigning Multiple Variables
x, y, z = 10, 20, 30

print("X:", x)
print("Y:", y)
print("Z:", z)

# 6. Assigning Same Value
a = b = c = 50

print(a)
print(b)
print(c)

# 7. Variable Calculations
number1 = 100
number2 = 50

total = number1 + number2
difference = number1 - number2

print("Total:", total)
print("Difference:", difference)

# 8. Increasing Variable Values
count = 10
count += 5

print("Count:", count)

# 9. Decreasing Variable Values
count -= 3
print("Updated Count:", count)

# 10. Swapping Variables
first_name = "Abebe"
second_name = "Kebede"

first_name, second_name = second_name, first_name

print("First:", first_name)
print("Second:", second_name)

# 11. Variable Naming Examples
student_id = 1001
total_marks = 450
employee_salary = 25000
product_price = 500

print(student_id)
print(total_marks)
print(employee_salary)
print(product_price)

# 12. Global and Local Variables
school = "ABC University"

def show_student():
    student = "Abebe"
    print("Student:", student)
    print("School:", school)

show_student()

# 13. Real World Example
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport = float(input("Enter transport allowance: "))
food = float(input("Enter food allowance: "))

gross_salary = basic_salary + transport + food

print("==============================")
print("       EMPLOYEE PAYSLIP       ")
print("==============================")
print("Employee:", employee_name)
print("Basic Salary:", basic_salary)
print("Transport:", transport)
print("Food:", food)
print("Gross Salary:", gross_salary)
print("==============================")

# END OF TOPIC 02
