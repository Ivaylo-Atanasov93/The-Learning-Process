n = int(input())
l = int(input())

for a in range(1, n):
    for b in range(1, n):
        for c in range(97, l + 97):
            for d in range(97, l + 97):
                for e in range(2, n + 1):
                    if e > a and e > b:
                        print(f'{a}{b}{chr(c)}{chr(d)}{e} ', end='')
