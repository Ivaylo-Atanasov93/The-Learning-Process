string = input().split()
not_money = False
while not not_money:
    command = input().split()
    if command[0] == "OutOfStock":
        if command[1] in string:
            for i in range(len(string)):
                if string[i] == str(command[1]):
                    string[i] = 'None'

    elif command[0] == 'Required':
        if int(command[2]) < len(string):
            string[int(command[2])] = command[1]

    elif command[0] == 'JustInCase':
        string.pop()
        string.append(command[1])
    elif command[0] == 'No' and command[1] == 'Money':
        not_money = True
        break

for i in string:
    if i != 'None':
        print(i, end=' ')