x = int(input())
y = int(input())
m = int(input())

counter = 0
flag = False
for i in range(x, y + 1):
    for j in range(x, y + 1):
        counter += 1
        if i + j == m:
            print(f'Combination N:{counter} ({i} + {j} = {m})')
            flag = True
    if flag:
        break

if not flag:
    print(f'{counter} combinations - neither equals {m}')