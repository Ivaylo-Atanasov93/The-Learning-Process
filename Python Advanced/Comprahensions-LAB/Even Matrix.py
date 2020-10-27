rows = int(input())
matrix = [list(input().split(', ')) for i in range(rows)]
matrix = [[int(num) for num in row if int(num) % 2 == 0] for row in matrix]
print(matrix)