days = int(input())
cookers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes_price = 45.00
waffles_price = 5.80
pancakes_price = 3.20

sumOfTheCakes = ((cookers * cakes) * cakes_price)
sumOfTheWaffles = ((cookers * waffles) * waffles_price)
sumOfThePancakes = ((cookers * pancakes) * pancakes_price)

prodPerDay = sumOfTheCakes + sumOfTheWaffles + sumOfThePancakes
wholeProd = prodPerDay * days

netProfit = wholeProd * 0.875

print(f'{netProfit:.2f}')