floors = int(input())
units = int(input())
floor_counter = floors
unit_counter = 0

while floor_counter > 0:
    while unit_counter < units:
        if floor_counter == floors:
            print(f'L{floor_counter}{unit_counter} ', end='')
        elif floor_counter % 2 == 0:
            print(f'O{floor_counter}{unit_counter} ', end='')
        else:
            print(f'A{floor_counter}{unit_counter} ', end='')
        unit_counter += 1
    unit_counter = 0
    floor_counter -= 1
    print()

