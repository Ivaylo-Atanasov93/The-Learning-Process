puzzle = 2.60
doll = 3.00
teddyBear = 4.10
minion = 8.20
truck = 2.00
vacPrice = float(input())
npuzzle = int(input())
ndolls = int(input())
nteddybear = int(input())
nminions = int(input())
ntrucks = int(input())
sumOfTheOrder = (npuzzle * puzzle) + (ndolls * doll) + (nteddybear * teddyBear) + (nminions * minion) + (ntrucks * truck)
sumOfTheToys = npuzzle + ndolls + nteddybear + nminions + ntrucks
discount = 1

if sumOfTheToys >= 50:
    discount = discount * 0.75


sumOfTheOrder = sumOfTheOrder * discount
sumOfTheOrder = sumOfTheOrder * 0.9

if sumOfTheOrder >= vacPrice:
    print(f'Yes! {sumOfTheOrder - vacPrice:.2f} lv left.')
else:
    print(f'Not enough money! {vacPrice - sumOfTheOrder:.2f} lv needed.')