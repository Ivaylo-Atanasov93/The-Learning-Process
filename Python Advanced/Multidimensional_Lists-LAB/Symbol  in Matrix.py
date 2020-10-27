rows = int(input())

matrix = []

for i in range(rows):
    row = [symbol for symbol in input()]
    matrix.append(row)

symbol = input()
occurred = False

for row in range(rows):
    for column in range(rows):
        current_symbol = matrix[row][column]
        if current_symbol == symbol:
            occurred = True
            print((row, column))
            break
    if occurred:
        break

if not occurred:
    print(f'{symbol} does not occur in the matrix')
