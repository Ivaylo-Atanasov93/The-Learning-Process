import math
numbers = list(map(int, input().split(', ')))
max_num = max(numbers)
lists = [[] for i in range(math.ceil(max_num / 10))]


for i in range(1, len(lists) + 1):
    max = i * 10
    min = i * 10 - 10
    for num in numbers:
        if min < num <= max:
            lists[i - 1].append(num)

for i in range(len(lists)):
    print(f"Group of {i + 1}0's: {lists[i]}")








'''
import math
numbers = list(map(int, input().split(', ')))
numbers.sort()
max_num = numbers[-1]
lists = [[] for i in range(math.ceil(max_num / 10))]
for i in range(len(lists)):
    for j in range(len(numbers)):
        if numbers[0] <= (i + 1) * 10:
            lists[i].append(numbers[0])
            numbers.pop(0)

for i in range(len(lists)):
    print(f"Group of {i + 1}0's: {lists[i]}")
'''