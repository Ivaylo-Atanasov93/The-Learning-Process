def adding(people):
    composition[-1] = composition[-1] + people
    return composition


def inserting(wagon, people):
    composition[wagon] = composition[wagon] + people
    return composition


def leaving(wagon, people):
    composition[wagon] = composition[wagon] - people
    return composition


wagons = int(input())
composition = [0 for i in range(wagons)]
command = ''

while command != 'End':
    command = input().split()
    if command[0] == 'add':
        adding(int(command[1]))
    elif command[0] == 'insert':
        inserting(int(command[1]), int(command[2]))
    elif command[0] == 'leave':
        leaving(int(command[1]), int(command[2]))
    elif command[0] == 'End':
        break

print(composition)
