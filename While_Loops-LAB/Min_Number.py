import sys
n = int(input())
counter = 1
min_number = sys.maxsize
while counter <= n:
    number = int(input())
    counter = counter + 1
    if number < min_number:
        min_number = number

print(min_number)