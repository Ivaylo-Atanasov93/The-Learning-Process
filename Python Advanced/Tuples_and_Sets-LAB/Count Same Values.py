sequence = input().split()
counter = {}

for num in sequence:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

for (key, value) in counter.items():
    print(f'{float(key)} - {value} times')
