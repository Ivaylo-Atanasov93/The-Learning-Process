rows = int(input())
matrix = [list(input().split(', ')) for i in range(rows)]
num_list = []
matrix = [[num_list.append(int(num)) for num in row] for row in matrix]
print(num_list)