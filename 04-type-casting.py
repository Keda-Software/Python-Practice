
# ==========================================
# PYTHON COURSE - TOPIC 04
# TYPE CASTING / TYPE CONVERSION
# ==========================================

# 1. String to Integer
age = "25"

print("Original:", age)
print("Original Type:", type(age))

age = int(age)

print("Converted:", age)
print("New Type:", type(age))

# 2. String to Float
price = "150.75"

print("\nString to Float")

price = float(price)

print("Price:", price)
print("Type:", type(price))

# 3. Integer to Float
number = 100

converted_number = float(number)

print("\nInteger to Float")
print(converted_number)
print(type(converted_number))

# 4. Float to Integer
decimal_number = 25.89

whole_number = int(decimal_number)

print("\nFloat to Integer")
print(whole_number)
print(type(whole_number))

# Note: int() removes the decimal part.
# It does not round the number.

# 5. Integer to String
student_id = 1001

student_id = str(student_id)

print("\nInteger to String")
print(student_id)
print(type(student_id))

# 6. Float to String
salary = 25000.50

salary = str(salary)

print("\nFloat to String")
print(salary)
print(type(salary))

# 7. Boolean Conversion
print("\nBoolean Conversion")

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool(100))

# 8. List Conversion
name = "PYTHON"

letters = list(name)

print("\nString to List")
print(letters)

# 9. List to Tuple
numbers = [10, 20, 30, 40]

converted_tuple = tuple(numbers)

print("\nList to Tuple")
print(converted_tuple)

# 10. List to Set
values = [10, 20, 10, 30, 20]

unique_values = set(values)

print("\nList to Set")
print(unique_values)

# 11. User Input Conversion
print("\nUSER INPUT EXAMPLE")

user_age = input("Enter your age: ")

user_age = int(user_age)

print("Your age is:", user_age)
print("Next year you will be:", user_age + 1)

# 12. Calculate Shopping Total
print("\nSHOPPING CALCULATOR")

product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_price = product_price * quantity

print("Total Price:", total_price)

# 13. Student Average Calculator
print("\nSTUDENT AVERAGE")

mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total:", total)
print("Average:", average)

# 14. Final Result
print("\n===== END OF TOPIC 04 =====")
