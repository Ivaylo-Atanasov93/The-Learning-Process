flower_type = input()
number = int(input())
budget = int(input())

item = 1
discount = 1
final_price = 0

if flower_type == 'Roses':
    item = item * 5.00
    if number > 80:
        discount = discount * 0.9

elif flower_type == 'Dahlias':
    item = item * 3.80
    if number > 90:
        discount = discount * 0.85

elif flower_type == 'Tulips':
    item = item * 2.80
    if number > 80:
        discount = discount * 0.85

elif flower_type == 'Narcissus':
    item = item * 3.00
    if number < 120:
        discount = discount * 1.15

elif flower_type == 'Gladiolus':
    item = item * 2.50
    if number < 80:
        discount = discount * 1.2

final_price = (item * number) * discount

if final_price <= budget:
    print(f'Hey, you have a great garden with {number} {flower_type} and {budget - final_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {final_price - budget:.2f} leva more.')