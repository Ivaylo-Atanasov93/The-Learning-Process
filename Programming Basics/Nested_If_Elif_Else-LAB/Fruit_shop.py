fruit = input()
day = input()
quantity = float(input())

price = 0

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = price + 2.5
    elif fruit == 'apple':
        price = price + 1.20
    elif fruit == 'orange':
        price = price + 0.85
    elif fruit == 'grapefruit':
        price = price + 1.45
    elif fruit == 'kiwi':
        price = price + 2.70
    elif fruit == 'pineapple':
        price = price + 5.50
    elif fruit == 'grapes':
        price = price + 3.85
    elif fruit == 0:
        print('error')

elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = price + 2.70
    elif fruit == 'apple':
        price = price + 1.25
    elif fruit == 'orange':
        price = price + 0.90
    elif fruit == 'grapefruit':
        price = price + 1.60
    elif fruit == 'kiwi':
        price = price + 3.00
    elif fruit == 'pineapple':
        price = price + 5.60
    elif fruit == 'grapes':
        price = price + 4.20
    elif fruit == 0:
        print('error')

if price != 0:
    print(f'{price * quantity:.2f}')
else:
    print('error')