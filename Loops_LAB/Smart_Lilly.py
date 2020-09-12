age = int(input())
washingmachine_price = float(input())
priceOfTheToy = float(input())

toyPresents = 0
moneyPresents = 0
savings = 0
moneyFromToys = 0
sum = 0
#2 - 10
#4 - 20
#6 - 30

for i in range(1, age + 1):
    if i % 2 == 0:
        moneyPresents = (i * 10) / 2
        moneyPresents = moneyPresents - 1
        savings = savings + moneyPresents
    else:
        toyPresents = toyPresents + 1

moneyFromToys = toyPresents * priceOfTheToy
sum = moneyFromToys + savings


if sum >= washingmachine_price:
    print(f'Yes! {sum - washingmachine_price:.2f}')
else:
    print(f'No! {washingmachine_price - sum:.2f}')
