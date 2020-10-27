def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def boom(row, col, playground):
    boom_row = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    boom_col = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    strenght = playground[row][col]
    if strenght > 0:
        for i in range(9):
            adress = row + boom_row[i], col + boom_col[i]
            if is_valid(adress, dimensions) and playground[adress[0]][adress[1]] > 0:
                playground[adress[0]][adress[1]] -= strenght


dimensions = int(input())
playground = []
active_cells = 0
active_cells_sum = 0

for i in range(dimensions):
    playground.append([int(number) for number in input().split()])

bombs = input().split()
bombs = [bomb.split(',') for bomb in bombs]

for bomb in bombs:
    boom(int(bomb[0]), int(bomb[1]), playground)

for i in range(dimensions):
    for j in range(dimensions):
        if playground[i][j] > 0:
            active_cells += 1
            active_cells_sum += playground[i][j]

print(f'Alive cells: {active_cells}')
print(f'Sum: {active_cells_sum}')
for row in playground:
    [print(element, end=' ') for element in row]
    print()
