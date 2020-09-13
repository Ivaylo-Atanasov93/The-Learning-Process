number = input()
sum = 0
while number != 'Stop':
    number = int(number)
    sum = sum + number
    number = input()

print(sum)