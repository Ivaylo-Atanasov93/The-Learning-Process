from collections import defaultdict
string = input()
counter = defaultdict(int)

for char in string:
    counter[char] += 1

[print(f'{key}: {value} time/s') for (key, value) in sorted(counter.items())]