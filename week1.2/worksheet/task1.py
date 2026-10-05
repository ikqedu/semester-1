# Worksheet 1.2: Task 1 Solution

grade = input("Enter an integer grade in the range 0 to 100\nYour grade: ")

if not (grade.isdigit() and 0 < int(grade) < 100):
    exit("Error: Grade must be an integer between 0 and 100")
grade = int(grade)

if 0 < grade < 39:
    print(f"{grade} is a Fail")
elif 40 < grade < 69:
    print(f"{grade} is a Pass")
elif 70 < grade < 100:
    print(f"{grade} is a Distinction")

""""
      82 is a Distinction
      57 is a Pass
      36 is a Fail

  - Fail = 0-39
  - Pass = 40-69
  - Distinction = 70-100
"""
