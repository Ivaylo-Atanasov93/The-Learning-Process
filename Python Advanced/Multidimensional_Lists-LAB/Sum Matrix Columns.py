(row_counts, column_counts) = [int(x) for x in input().split(', ')]
matrix = []

for i in range(row_counts):
    row = [int(num) for num in input().split()]
    matrix.append(row)

matrix_column_sum = [0] * column_counts

for i in range(row_counts):
    for j in range(column_counts):
        matrix_column_sum[j] += matrix[i][j]

[print(element) for element in matrix_column_sum]