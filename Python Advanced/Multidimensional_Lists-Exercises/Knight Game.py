def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def knights_for_killing(row, col, size, matrix):
    killed_knights = 0
    rows = [-2, -2, -1, -1, 1, 1, 2, 2]
    cols = [-1, 1, -2, 2, -2, 2, -1, 1]
    for i in range(8):
        current_pos = row + rows[i], col + cols[i]
        if is_valid(current_pos, size) and matrix[current_pos[0]][current_pos[1]] == 'K':
            killed_knights += 1
    return killed_knights


size = int(input())
matrix = []
all_rem_knights = 0

for i in range(size):
    matrix.append([symbol for symbol in input()])



while True:
    current_kill = 0
    to_kill = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                killed_knights = knights_for_killing(row, col, size, matrix)
                if killed_knights > current_kill:
                    current_kill = killed_knights
                    to_kill = [row, col]

    if current_kill == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    matrix[to_kill_row][to_kill_col] = '0'
    all_rem_knights += 1

#[print(row) for row in matrix]
print(all_rem_knights)

