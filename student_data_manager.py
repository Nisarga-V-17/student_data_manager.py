# Student Data Manager

# Dictionary storing student names and marks
students = {
    "Aarav": 85,
    "Diya": 92,
    "Rohan": 78,
    "Meera": 88,
    "Kabir": 95
}

# Find topper
topper = max(students, key=students.get)

# Calculate class average
average = sum(students.values()) / len(students)

# Function to assign grades
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

print("Student Grades:\n")

for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name}: Marks = {marks}, Grade = {grade}")

print("\nTopper:", topper, "-", students[topper])
print("Class Average:", round(average, 2))