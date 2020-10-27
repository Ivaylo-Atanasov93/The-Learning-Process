from collections import defaultdict
miners = defaultdict(int)
while True:
    string = input()
    if string == 'stop':
        break
    value = int(input())
    miners[string] += value

for mine in miners:
    print(f'{mine} -> {miners[mine]}')