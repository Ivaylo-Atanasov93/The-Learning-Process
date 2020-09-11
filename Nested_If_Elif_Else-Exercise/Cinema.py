screening_type = input()
rows = int(input())
columns = int(input())

income = 0

if screening_type == 'Premiere':
    income = 12 * (rows * columns)
elif screening_type == 'Normal':
    income = 7.5 * (rows * columns)
elif screening_type == 'Discount':
    income = 5 * (rows * columns)

print(f'{income:.2f} leva')