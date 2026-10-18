
# Student Grade Management System

name = input("Enter student name: ")

mark1 = float(input("Enter mark for Python: "))
mark2 = float(input("Enter mark for Database: "))
mark3 = float(input("Enter mark for Networking: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n--- Student Result ---")
print("Name:", name)
print("Average:", round(average, 2))
print("Grade:", grade)

if average >= 50:
    print("Status: PASS")
else:
    print("Status: FAIL")
