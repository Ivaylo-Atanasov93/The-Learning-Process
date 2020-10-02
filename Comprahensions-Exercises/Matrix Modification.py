def is_valid(row, col):
    return 0 <= row <= dimensions - 1 and 0 <= col <= dimensions - 1


dimensions = int(input())
matrix = [input().split() for i in range(dimensions)]
matrix = [[int(matrix[i][j]) for j in range(dimensions)] for i in range(dimensions)]
not_end = True

while not_end:
    command = input().split()
    if command[0] == 'END':
        not_end = False
        break
    action = command[0]
    (row, col) = int(command[1]), int(command[2])
    number = int(command[3])
    if is_valid(row, col):
        if action == 'Add':
            matrix[row][col] = matrix[row][col] + number
        elif action == 'Subtract':
            matrix[row][col] = matrix[row][col] - number
    else:
        print('Invalid coordinates')

# for i in range(dimensions):
#     if i > 0:
#         print()
#     for j in range(dimensions):
#         print(matrix[i][j], end=' ')

[print(' '.join(str(row).strip('[]').split(', ')))for row in matrix]
