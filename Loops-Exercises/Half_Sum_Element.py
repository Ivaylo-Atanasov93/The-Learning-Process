import sys
n = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(0, n):
    num = int(input())
    sum = sum + num
    if num > max_num:
        max_num = num

sum = sum - max_num
if max_num == sum:
    print('Yes')
    print(f'Sum = {sum}')
else:
    print('No')
    print(f'Diff = {abs(sum - max_num)}')
