(rows_count, columns_count) = [int(x) for x in input().split()]
snake = input()
counter = 0
counter_stop = len(snake)
for i in range(rows_count * columns_count):
    snake += snake[counter]
    counter += 1
    if counter == counter_stop:
        counter = 0

matrix = []
snake_counter = 0
for i in range(rows_count):
    matrix.append([0 for j in range(columns_count)])

for i in range(rows_count):
    for j in range(1, columns_count + 1):
        if i % 2 == 0:
            matrix[i][j - 1] = snake[snake_counter]
            snake_counter += 1
        else:
            matrix[i][-j] = snake[snake_counter]
            snake_counter += 1

for i in range(rows_count):
    for j in range(columns_count):
        print(matrix[i][j], end='')
        if j == columns_count - 1:
            print()
