n = int(input())

even_numbers = 0
odd_numbers = 0

for i in range(0, n):
    number = int(input())
    if i % 2 == 0:
        even_numbers = even_numbers + number
    else:
        odd_numbers = odd_numbers + number

if odd_numbers == even_numbers:
    print(f'Yes')
    print(f'Sum = {even_numbers}')
else:
    print('No')
    print(f'Diff = {abs(even_numbers - odd_numbers)}')