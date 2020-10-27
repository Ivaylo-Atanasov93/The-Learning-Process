hour = int(input())
minutes = int(input())

minutes = minutes + 15

if minutes >= 60:
    hour = hour + 1
    minutes = minutes - 60
    if hour >23:
        hour = hour - hour
    if minutes < 10:
        print(f'{hour}:0{minutes}')
    else:
        print(f'{hour}:{minutes}')
else:
    if minutes < 10:
        print(f'{hour}:0{minutes}')
    else:
        print(f'{hour}:{minutes}')