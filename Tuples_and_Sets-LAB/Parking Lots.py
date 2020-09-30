commands = int(input())
parking_lot = set()

for _ in range(commands):
    (command, plate) = input().split(', ')
    if command == 'IN':
        parking_lot.add(plate)
    else:
        parking_lot.discard(plate)

if parking_lot:
    [print(plate) for plate in parking_lot]
else:
    print('Parking Lot is Empty')