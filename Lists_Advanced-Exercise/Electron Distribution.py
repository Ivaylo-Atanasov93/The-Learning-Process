number = int(input())
slot_list = []
n = 1

while number > 0:
    if number >= 2 * n ** 2:
        slot_list.append(2 * n ** 2)
        number -= 2 * n ** 2
        n += 1
    else:
        slot_list.append(number)
        number -= number

print(slot_list)