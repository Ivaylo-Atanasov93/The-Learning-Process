(row_counts, column_counts) = [int(x) for x in input().split(', ')]
matrix = []

for i in range(row_counts):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)

matrix_sum = 0

for row in matrix:
    matrix_sum += sum(row)

print(matrix_sum)
print(matrix)