import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

lenght = abs(x1 - x2)
width = abs(y1 - y2)

area = (lenght * width)
perimeter = 2 * lenght + 2 * width

print(f'{area:.2f}')
print(f'{perimeter:.2f}')