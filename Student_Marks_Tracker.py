student = {}

num_student = int(input("Enter the number of students you want to add: "))

for i in range(num_student):
    name = input("Enter the name of the student: ")
    marks = []
    num_subjects = int(input("Enter the number of subjects: "))
    for j in range(num_subjects):
        m = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(m)
    student[name] = marks

print("\nDisplay all students:")
for name, marks in student.items():
    print(f"Name: {name}, Marks: {marks}")

print("\nAverage of student marks:")
for name, marks in student.items():
    avg = sum(marks) / len(marks)
    print(f"{name}'s average marks is {avg:.2f}")

highest_scored_student = None
highest_marks = -1
highest_subject = None

for name, marks in student.items():
    for i, mark in enumerate(marks, start=1):
        if mark > highest_marks:
            highest_scored_student = name
            highest_marks = mark
            highest_subject = i

print(f"\nHighest scored student is {highest_scored_student} in subject {highest_subject} with marks {highest_marks}")
