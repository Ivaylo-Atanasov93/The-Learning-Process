jury = int(input())
presentation = ''
grade = 0.00
sum_grade_per_presentation = 0
average_grade_per_presentation = 0
sum_of_all_grades = 0
#average_grade = 0
presentation_counter = 0

while presentation != 'Finish':
    sum_of_all_grades += average_grade_per_presentation
    sum_grade_per_presentation = 0
    average_grade_per_presentation = 0
    presentation = input()
    if presentation == 'Finish':
        average_grade = sum_of_all_grades / presentation_counter
        print(f'Student\'s final assessment is {average_grade:.2f}.')
        break
    else:
        presentation_counter += 1
        for i in range(0, jury):
            grade = float(input())
            sum_grade_per_presentation += grade
            average_grade_per_presentation = sum_grade_per_presentation / jury

        print(f'{presentation} - {average_grade_per_presentation:.2f}.')

