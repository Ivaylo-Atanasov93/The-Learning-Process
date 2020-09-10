import math
income = float(input())
avGrade = float(input())
minSal = float(input())
amountOfSoc = 0
amountOfGr = 0


if income < minSal:
    if avGrade > 4.5:
        amountOfSoc = minSal * 0.35
    elif avGrade >= 5.5:
        amountOfGr = avGrade * 25
    else:
        print('You cannot get a scholarship!')
else:
    if avGrade >= 5.5:
        amountOfGr = avGrade * 25
    else:
        print('You cannot get a scholarship!')

if amountOfGr >= amountOfSoc and amountOfGr != 0:
    print(f'You get a scholarship for excellent results {math.floor(amountOfGr)} BGN')

elif amountOfSoc > amountOfGr:
    print(f'You get a Social scholarship {math.floor(amountOfSoc)} BGN')

