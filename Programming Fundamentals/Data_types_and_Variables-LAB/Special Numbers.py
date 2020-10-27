number = int(input())
for i in range(1, number + 1):
    sum_of_digits = 0
    for j in str(i):
        digit = int(j)
        sum_of_digits = sum_of_digits + digit

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')