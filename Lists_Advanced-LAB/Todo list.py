running = True
todo_list = [0 for i in range(10)]
while running:
    command = input()
    if command == 'End':
        running = False
    else:
        tokens = command.split('-')
        index = int(tokens[0]) - 1
        todo_list[index] = tokens[1]

todo_list = [note for note in todo_list if note != 0]
print(todo_list)