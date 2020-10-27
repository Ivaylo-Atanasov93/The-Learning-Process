import math
width = float(input())
length = float(input())
height = float(input())

room_cubic_meters = width * length * height
boxes_sum = 0
number = 0
done = False
while boxes_sum <= room_cubic_meters and done == False:
    number = input()
    if number == 'Done':
        print(f'{(math.floor(room_cubic_meters - boxes_sum))} Cubic meters left.')
        done = True
    else:
        number = int(number)
        boxes_sum = boxes_sum + number


if boxes_sum >= room_cubic_meters:
    print(f'No more free space! You need {math.floor(boxes_sum - room_cubic_meters)} Cubic meters more.')