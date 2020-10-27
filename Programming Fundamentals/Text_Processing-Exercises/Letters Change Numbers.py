line = input().split()
sum = 0
for element in line:
    first = element[0]
    last = element[-1]
    num = int(element[1:-1])
    if first.isupper():
        sum += num / (ord(first) - 64)

    elif first.islower():
        sum += num * (ord(first) - 96)

    if last.isupper():
        sum -= ord(last) - 64
    elif last.islower():
        sum += ord(last) - 96

print(f'{sum:.2f}')
