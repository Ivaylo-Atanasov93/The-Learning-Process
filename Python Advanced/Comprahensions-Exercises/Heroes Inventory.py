heroes = {name: {} for name in input().split(', ')}
not_end = True

while not_end:
    command = input()
    if command == 'End':
        not_end = False
        break
    name = command.split('-')[0]
    item = command.split('-')[1]
    cost = int(command.split('-')[2])
    if item not in heroes[name]:
        heroes[name][item] = cost

[print(f'{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}') for name in heroes]