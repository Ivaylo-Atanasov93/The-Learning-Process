import math
hour_of_the_exam = int(input())
minute_of_the_exam = int(input())
arriving_hour = int(input())
arriving_minute = int(input())

hoursInMinutesExam = 0
hoursInMinutesArrive = 0

hoursInMinutesExam = hour_of_the_exam * 60
hoursInMinutesArrive = arriving_hour * 60

examTimeInMinutes = hoursInMinutesExam + minute_of_the_exam
arrivingTimeInMinutes = hoursInMinutesArrive + arriving_minute

difference = examTimeInMinutes - arrivingTimeInMinutes
differenceInHours = 0
differenceInMin = 0

if examTimeInMinutes >= arrivingTimeInMinutes:                                              # ON TIME SECTION
    if arrivingTimeInMinutes == examTimeInMinutes:
        print('On time')

    elif arrivingTimeInMinutes >= examTimeInMinutes - 30:
        print('On Time')
        print(f'{examTimeInMinutes - arrivingTimeInMinutes} minutes before the start')

    elif arrivingTimeInMinutes < examTimeInMinutes - 30:                                   # EARLY SECTION
        print('Early')

        if examTimeInMinutes - arrivingTimeInMinutes <= 59:
            print(f'{examTimeInMinutes - arrivingTimeInMinutes} minutes before the start')

        else:
            differenceInHours = difference / 60
            differenceInMin = difference - (math.floor(differenceInHours) * 60)

            if differenceInMin < 10:
                print(f'{math.floor(abs(differenceInHours))}:0{differenceInMin} hours before the start')

            else:
                print(f'{math.floor(abs(differenceInHours))}:{differenceInMin} hours before the start')

elif examTimeInMinutes < arrivingTimeInMinutes:                                              # LATE SECTION

    if arrivingTimeInMinutes - examTimeInMinutes <= 59:
        print('Late')
        print(f'{arrivingTimeInMinutes - examTimeInMinutes} minutes after the start')

    else:
        print('Late')
        differenceInHours = difference / 60
        differenceInMin = difference - (math.floor(differenceInHours) * 60)

        if differenceInMin < 10:
            print(f'{math.floor(abs(differenceInHours))}:0{differenceInMin} hours after the start')

        else:
            print(f'{math.floor(abs(differenceInHours))}:{differenceInMin} hours after the start')