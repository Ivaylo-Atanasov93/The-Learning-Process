from collections import defaultdict


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, format(v, '.2f')))


item_price = defaultdict(float)
item_quantity = defaultdict(int)

buyed = False

while not buyed:
    order = input().split()
    if order[0] == 'buy':
        buyed = True
        break
    item_price[order[0]] = float(order[1])
    item_quantity[order[0]] += int(order[2])

final_order = {}

for item in item_price:
    final_order[item] = item_price[item] * item_quantity[item]

print_dict(final_order, '{} -> {}')
