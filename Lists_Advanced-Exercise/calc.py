a = 1
years = int(input('Input the term of the investments: '))
amount = 2678

for i in range(years):
    last_year_amount = amount
    amount += (amount * a)
    print(f'Amount increase for the year: {amount - last_year_amount:.2f}')

print(f'{amount:.2f}')