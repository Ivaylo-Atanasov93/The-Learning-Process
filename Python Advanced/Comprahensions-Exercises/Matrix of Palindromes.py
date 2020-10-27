rows, cols = [int(num) for num in input().split()]
letters = [chr(i) for i in range(97, 123)]
matrix = [[f'{letters[j]}{letters[i + j]}{letters[j]}' for i in range(cols)] for j in range(rows)]
[print(' '.join(row)) for row in matrix]