student_name = input()
counter = 1
avg_grade = 0

while counter <= 12:
    grade = float(input())
    if grade >= 4.00:
        avg_grade = avg_grade + grade
        counter = counter + 1
    else:
        continue

print(f"{student_name} graduated. Average grade: {avg_grade / 12:.2f}")