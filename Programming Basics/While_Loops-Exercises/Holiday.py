holiday_price = float(input())
balance = float(input())

spent_counter = 0
counter = 0

while balance < holiday_price and spent_counter < 5:

    saved_or_spent = input()
    saved_or_spent_money = float(input())
    counter += 1

    if saved_or_spent == 'spend':
        balance = balance - saved_or_spent_money
        spent_counter += 1
        if balance < 0:
            balance = 0


    elif saved_or_spent == 'save':
        balance = balance + saved_or_spent_money
        spent_counter = 0


if spent_counter == 5:
    print(f"You can't save the money.")
    print(f'{counter}')
elif balance >= holiday_price:
    print(f'You saved the money for {counter} days.')