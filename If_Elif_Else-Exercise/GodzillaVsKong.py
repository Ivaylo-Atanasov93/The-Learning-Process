budget = float(input())
statists = int(input())
clothesForStatist = float(input())

decor = budget * 0.1

if statists > 150:
    clothesForStatist = clothesForStatist * 0.9
else: clothesForStatist = clothesForStatist * 1

sumOfClodhes = clothesForStatist * statists

movieCosts = decor + sumOfClodhes

if budget >= movieCosts:
    print('Action!')
    print(f'Wingard starts filming with {budget - movieCosts:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {movieCosts - budget:.2f} leva more.')