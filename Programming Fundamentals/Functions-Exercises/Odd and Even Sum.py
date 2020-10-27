def summing_odd_and_even(string):
    even_sum = 0
    odd_sum = 0
    for i in range(len(string)):
        if int(string[i]) % 2 == 0:
            even_sum += int(string[i])
        else:
            odd_sum += int(string[i])

    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')



line = input()
summing_odd_and_even(line)
