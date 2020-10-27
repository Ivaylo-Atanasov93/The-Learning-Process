line = input().split()
string_one = line[0]
string_two = line[1]
sum = 0
difference = 0

if len(string_one) < len(string_two):
    iterations = len(string_one)
    difference = len(string_two) - len(string_one)
else:
    iterations = len(string_two)
    difference = len(string_one) - len(string_two)

for i in range(iterations):
    if ord(string_one[i]) == 0:
        sum += ord(string_two[i])
    elif ord(string_two[i]) == 0:
        sum += ord(string_one[i])
    else:
        sum += ord(string_one[i]) * ord(string_two[i])

if iterations == len(string_one) and difference > 0:
    for i in range(1, difference + 1):
        sum += ord(string_two[-i])
else:
    for i in range(1, difference + 1):
        sum += ord(string_one[-i])

print(sum)