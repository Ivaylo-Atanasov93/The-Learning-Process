(row_counts, column_counts) = [int(x) for x in input().split(', ')]
matrix = []

for i in range(row_counts):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)

max_sum = 0
starting_point = []

for i in range(row_counts - 1):
    for j in range(column_counts - 1):
        current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            starting_point.clear()
            starting_point.append(i)
            starting_point.append(j)

print(matrix[starting_point[0]][starting_point[1]], matrix[starting_point[0]][starting_point[1] + 1])
print(matrix[starting_point[0] + 1][starting_point[1]], matrix[starting_point[0] + 1][starting_point[1] + 1])
print(max_sum)

