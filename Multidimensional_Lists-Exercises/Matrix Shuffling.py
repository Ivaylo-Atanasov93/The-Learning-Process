(rows, columns) = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([element for element in input().split()])

end = False

while not end:
    command = input().split()
    if command[0] == 'END':
        end = True
        break
    elif command[0] == 'swap' and len(command) == 5:
        f_e_address = [int(command[1]), int(command[2])]
        s_e_address = [int(command[3]), int(command[4])]
        if f_e_address[0] > rows - 1 or f_e_address[1] > columns - 1 or \
                s_e_address[0] > rows - 1 or s_e_address[1] > columns - 1:
            print('Invalid input!')
        else:
            matrix[f_e_address[0]][f_e_address[1]], matrix[s_e_address[0]][s_e_address[1]] = \
                matrix[s_e_address[0]][s_e_address[1]], matrix[f_e_address[0]][f_e_address[1]]
            for i in range(rows):
                for j in range(columns):
                    print(matrix[i][j], end=' ')
                    if j == columns - 1:
                        print()
    else:
        print('Invalid input!')
