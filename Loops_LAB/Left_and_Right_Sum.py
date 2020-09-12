n = int(input())

left_number = 0
right_number = 0

for i in range(0, n):
    number = int(input())
    left_number = left_number + number

for i in range(0, n):
    number = int(input())
    right_number = right_number + number

if left_number == right_number:
    print(f'Yes, sum = {left_number}')
else:
    print(f'No, diff = {abs(left_number - right_number)}')