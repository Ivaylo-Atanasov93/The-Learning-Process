items = input().split('|')
budget = float(input())
current_item = []
sale_prices = []
profit = 0

for i in range(len(items)):
    current_item = items[i].split('->')
    if current_item[0] == 'Clothes' and float(current_item[1]) <= 50 and float(current_item[1] < budget):
        budget -= float(current_item[1])
        sale_prices.append(float(current_item[1]) * 1.4)

    elif current_item[0] == 'Shoes' and float(current_item[1]) <= 35 and float(current_item[1] < budget):
        budget -= float(current_item[1])
        sale_prices.append(float(current_item[1]) * 1.4)

    elif current_item[0] == 'Accessories' and float(current_item[1]) <= 20.50 and float(current_item[1] < budget):
        budget -= float(current_item[1])
        sale_prices.append(float(current_item[1]) * 1.4)

    else:
        continue

profit_per_item = 1 / 1.4
for i in range(len(sale_prices)):
    profit += sale_prices[i] * profit_per_item
    print(profit_per_item)