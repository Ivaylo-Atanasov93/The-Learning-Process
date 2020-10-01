(rows_count, columns_count) = [int(x) for x in input().split()]
matrix = []

for _ in range(rows_count):
    matrix.append([symbol for symbol in input().split()])

squares = 0

for i in range(rows_count - 1):
    for j in range(columns_count - 1):
        if matrix[i][j] == matrix[i][j + 1] and \
                matrix[i][j] == matrix[i + 1][j] and \
                matrix[i][j] == matrix[i + 1][j + 1]:
                    squares += 1

print(squares)
