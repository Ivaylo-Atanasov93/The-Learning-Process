item = input()
town = input()
quantity = float(input())


if item == 'coffee':
    if town == 'Sofia':
        print(quantity * 0.5)
    elif town == 'Plovdiv':
        print(quantity * 0.4)
    else:
        print(quantity * 0.45)
elif item == 'water':
    if town == 'Sofia':
        print(quantity * 0.8)
    elif town == 'Plovdiv':
        print(quantity * 0.7)
    else:
        print(quantity * 0.7)
elif item == 'beer':
    if town == 'Sofia':
        print(quantity * 1.2)
    elif town == 'Plovdiv':
        print(quantity * 1.15)
    else:
        print(quantity * 1.1)
elif item == 'sweets':
    if town == 'Sofia':
        print(quantity * 1.45)
    elif town == 'Plovdiv':
        print(quantity * 1.30)
    else:
        print(quantity * 1.35)
elif item == 'peanuts':
    if town == 'Sofia':
        print(quantity * 1.6)
    elif town == 'Plovdiv':
        print(quantity * 1.50)
    else:
        print(quantity * 1.55)

