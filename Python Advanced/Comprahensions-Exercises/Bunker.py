categories = {category: {} for category in input().split(', ')}
num = int(input())
for i in range(num):
    command = input().split(' - ')
    details = command[2].split(';')
    category = command[0]
    item = command[1]
    quantity = int(details[0].split(':')[1])
    quality = int(details[1].split(':')[1])
    if item not in category:
        categories[category][item] = (quantity, quality)

quantity_sum = sum([sum([x[0] for x in list(categories[category].values())]) for category in categories])
avg_quality = sum([sum([x[1] for x in list(categories[category].values())]) for category in categories]) / sum(1 for category in categories)


print(f'Count of items: {quantity_sum}')
print(f'Average quality: {avg_quality:.2f}')
[print(f'{category} -> {", ".join(categories[category])}') for category in categories]
