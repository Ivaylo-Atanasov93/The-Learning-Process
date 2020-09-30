number_of_guests = int(input())
reservations = set()
[reservations.add(input()) for _ in range(number_of_guests)]
arrived_guests = set()
end = False

while not end:
    guest = input()
    if guest == 'END':
        end = True
        break
    else:
        if guest in reservations:
            arrived_guests.add(guest)

guests = list(sorted(reservations.difference(arrived_guests)))
print(len(guests))
[print(left) for left in guests]