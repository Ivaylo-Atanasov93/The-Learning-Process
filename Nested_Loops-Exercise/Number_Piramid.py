number = int(input())
current = 1

for i in range(1, number + 1):
    for j in range(1, i + 1):
        if current > number:
            break
        print(str(current) + ' ', end="")
        current += 1
    if current > number:
        break
    print()