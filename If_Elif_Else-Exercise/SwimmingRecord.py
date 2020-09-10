import math
recInSec = float(input())
distance = float(input())
secPerMet = float(input())

aditDelayTimes = distance / 15
aditDel = math.floor(aditDelayTimes) * 12.5
result = distance * secPerMet + aditDel

if result < recInSec:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')
else:
    print(f'No, he failed! He was {result - recInSec:.2f} seconds slower.')