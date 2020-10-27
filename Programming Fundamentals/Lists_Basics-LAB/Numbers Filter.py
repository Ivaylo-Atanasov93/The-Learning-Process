n = int(input())
numbers = []
filtered_numbers = []
for _ in range(0, n):
    number = int(input())
    numbers.append(number)

command = input()

if command == 'even':
    for i in numbers:
        if i % 2 == 0:
            filtered_numbers.append(i)
elif command == 'odd':
    for i in numbers:
        if i % 2 != 0:
            filtered_numbers.append(i)
elif command == 'positive':
    for i in numbers:
        if i >= 0:
            filtered_numbers.append(i)
elif command == 'negative':
    for i in numbers:
        if i < 0:
            filtered_numbers.append(i)

print(filtered_numbers)