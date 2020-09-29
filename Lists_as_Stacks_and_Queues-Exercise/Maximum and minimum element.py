stack = []
number = int(input())
for i in range(number):
    command = input()
    if command[0] == '1':
        stack.append(int(command[2:]))
    elif command == '2' and stack:
            stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))
print(str(stack[::-1]).strip('[]'))
