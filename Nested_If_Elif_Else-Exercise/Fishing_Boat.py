budget = float(input())
season = input()
number = int(input())

price = 0
discount = 1

if season == 'Spring':
    price = price + 3000
    if number <= 6:
        discount = discount * 0.9
    elif number <= 11:
        discount = discount * 0.85
    elif number > 11:
        discount = discount * 0.75
elif season == 'Summer' or season == 'Autumn':
    price = price + 4200
    if number <= 6:
        discount = discount * 0.9
    elif 6 < number <= 11:
        discount = discount * 0.85
    elif number > 11:
        discount = discount * 0.75
elif season == 'Winter':
    price = price + 2600
    if number <= 6:
        discount = discount * 0.9
    elif 6 < number <= 11:
        discount = discount * 0.85
    elif number > 11:
        discount = discount * 0.75

final_price = price * discount

if number % 2 == 0 and season != 'Autumn':
    final_price = final_price * 0.95

if budget >= final_price:
    print(f'Yes! You have {budget - final_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {final_price - budget:.2f} leva.')