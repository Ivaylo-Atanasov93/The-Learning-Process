from collections import defaultdict

num_of_students = int(input())
students = defaultdict(list)

for _ in range(num_of_students):
    student = input().split()
    students[student[0]].append(float(student[1]))

for (key, value) in students.items():
    avg_grades = sum(value) / len(value)
    grade_string = ' '.join(f'{grade:.2f}' for grade in value)
    print(f'{key} -> {grade_string} (avg: {avg_grades:.2f})')

# num_of_students = int(input())
# students = {}
#
# for _ in range(num_of_students):
#     student = input().split()
#     if student[0] in students:
#         students[student[0]].append(student[1])
#     else:
#         students[student[0]] = []
#         students[student[0]].append(student[1])
#
#
# print(students)
