dimensions = int(input())
matrix = []
first_diagonal = []
second_diagonal = []
[matrix.append([(int(num)) for num in input().split(', ')]) for i in range(dimensions)]
[first_diagonal.append(matrix[i][i]) for i in range(dimensions)]
[second_diagonal.append(matrix[i - 1][-i]) for i in range(1, dimensions + 1)]
print(f'First diagonal: {str(first_diagonal).strip("[]")}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {str(second_diagonal).strip("[]")}. Sum: {sum(second_diagonal)}')