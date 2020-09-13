import sys
n = int(input())
counter = 1
max_number = -sys.maxsize
while counter <= n:
    number = int(input())
    counter = counter + 1
    if number > max_number:
        max_number = number

print(max_number)