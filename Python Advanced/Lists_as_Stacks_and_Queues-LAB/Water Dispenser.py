def solve():
    queue = []
    counter = 0
    done = False
    liters = int(input())
    while not done:
        line = input()
        if line != 'Start':
            queue.append(line)
        elif line == 'Start':
            while True:
                command = input().split()
                if command[0] == 'refill':
                    liters += int(command[1])

                elif command[0] == 'End':
                    print(f'{liters} liters left')
                    done = True
                    break

                else:
                    if int(command[0]) <= liters:
                        counter = 0
                        print(f'{queue[counter]} got water')
                        liters -= int(command[0])
                        queue.pop(counter)
                    else:
                        print(f'{queue[counter]} must wait')
                        counter += 1


solve()
