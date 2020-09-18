multiplier = int(input())
diapason = int(input())
array = []
num = 1

while len(array) < diapason:
    if num % multiplier == 0:
        array.append(num)
    num += 1

print(array)