(rows_count, columns_count) = [int(x) for x in input().split()]
matrix = []
for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])

biggest_sum = 0
first_point = [0, 0]
for i in range(rows_count - 2):
    for j in range(columns_count - 2):

        current_matrix_sum = 0
        for k in range(3):
            for y in range(3):
                current_matrix_sum += matrix[i + k][j + y]

        if current_matrix_sum > biggest_sum:
            biggest_sum = current_matrix_sum
            first_point.clear()
            first_point.append(i)
            first_point.append(j)
    current_matrix_sum = 0

print(f'Sum = {biggest_sum}')
for i in range(3):
    if i > 0:
        print()
    for j in range(3):
        print(matrix[first_point[0] + i][first_point[1] + j], end=' ')
