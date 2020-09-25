storage = {}
while True:
    line = input().split(': ')
    if line[0] == 'statistics':
        break
    else:
        item = line[0]
        quantity = int(line[1])
        if item in storage:
            storage[item] += quantity
        else:
            storage[item] = quantity

print('Products in stock:')
for item in storage:
    print(f'- {item}: {storage[item]}')
print(f'Total Products: {len(storage)}')
print(f'Total Quantity: {sum(storage.values())}')