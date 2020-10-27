import math
year = input()
holidays = int(input())
homeWeekends = int(input())

weekends = 48
weekends_in_sofia = weekends - homeWeekends
free_weekends_in_sofia = (weekends_in_sofia / 4) * 3
free_holidays = (holidays / 3) * 2
sumOfThePlayingWeekends = free_holidays + free_weekends_in_sofia + homeWeekends

if year == 'leap':
    sumOfThePlayingWeekends = sumOfThePlayingWeekends * 1.15
    print(math.floor(sumOfThePlayingWeekends))


else:
    print(math.floor(sumOfThePlayingWeekends))