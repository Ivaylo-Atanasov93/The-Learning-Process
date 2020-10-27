import math
length = float(input())
width = float(input())
sideOfW = float(input())

areaOfTheHall = (length * 100) * (width * 100)
wardrobe = (sideOfW * 100) * (sideOfW * 100)
sittingSpace = areaOfTheHall / 10

clearSpace = areaOfTheHall - wardrobe - sittingSpace
numOfDancers = clearSpace / (40 + 7000)


print(f'{math.floor(numOfDancers)}')