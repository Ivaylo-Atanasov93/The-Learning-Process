installments  = int(input())
counter = 1
sum_of_the_amounts = 0
amount = 0

while counter <= installments:
    amount = float(input())
    if amount < 0:
        print('Invalid operation!')
        break
    else:
        sum_of_the_amounts = sum_of_the_amounts + amount
        counter = counter + 1
        print(f'Increase: {amount:.2f}')
print(f'Total: {sum_of_the_amounts:.2f}')
