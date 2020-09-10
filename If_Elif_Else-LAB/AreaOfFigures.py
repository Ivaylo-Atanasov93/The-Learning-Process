import math
figure = input()

if figure == 'square':
   side = float(input())
   area = side * side
elif figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
elif figure == 'circle':
    radius = float(input())
    area = math.pi * (radius * radius)
else:
    side1 = float(input())
    side2 = float(input())
    area = (side1 * side2) / 2

print(f'{area:.3f}')