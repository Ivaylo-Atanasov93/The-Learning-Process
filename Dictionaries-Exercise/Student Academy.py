from collections import defaultdict


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


students_count = int(input())
students = defaultdict(list)
to_go = defaultdict(list)

for i in range(students_count):
    name = input()
    grade = float(input())
    students[name].append(grade)

for student in students:
    if sum(students[student]) / len(students[student]) >= 4.50:
        to_go[student] = sum(students[student]) / len(students[student])

to_go = dict(sorted(to_go.items(), key=lambda x: -x[1]))
print_dict(to_go, '{} -> {:.2f}')
