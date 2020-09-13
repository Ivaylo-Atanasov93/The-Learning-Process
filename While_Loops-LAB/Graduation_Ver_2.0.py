student_name = input()
counter = 1
failure_counter = 0
grade = 0
avg_grade = 0

while counter <= 12 and failure_counter < 2:

    grade = float(input())

    if grade >= 4.00:
        counter = counter + 1
        avg_grade = avg_grade + grade

    else:
        failure_counter = failure_counter + 1
        if failure_counter == 2:
            break

if counter >= 12:
    print(f'{student_name} graduated. Average grade: {avg_grade / 12:.2f}')
elif failure_counter == 2:
    print(f'{student_name} has been excluded at {counter} grade')