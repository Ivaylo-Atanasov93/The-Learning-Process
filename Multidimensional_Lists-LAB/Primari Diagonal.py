rows = int(input())

matrix = []

for i in range(rows):
    row = [int(num) for num in input().split()]
    matrix.append(row)

diagonal_sum = 0

for i in range(rows):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)