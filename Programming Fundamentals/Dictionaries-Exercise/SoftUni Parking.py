def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


number_of_cars = int(input())
parking_slots = {}

for _ in range(number_of_cars):
    line = input().split()
    command = line[0]
    name = line[1]

    if command == 'register':
        plate = line[2]
        if name in parking_slots.keys():
            print(f"ERROR: already registered with plate number {parking_slots[name]}")
            continue
        parking_slots[name] = plate
        print(f'{name} registered {plate} successfully')

    elif command == 'unregister':
        if name not in parking_slots:
            print(f"ERROR: user {name} not found")
            continue
        parking_slots.pop(name)
        print(f"{name} unregistered successfully")

print_dict(parking_slots, '{} => {}')
