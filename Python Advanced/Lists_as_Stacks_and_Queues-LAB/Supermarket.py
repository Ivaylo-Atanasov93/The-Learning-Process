def solve():
    queue = []
    while True:
        line = input()
        if line == 'End':
            print(f"{len(queue)} people remaining.")
            break
        elif line == 'Paid':
            [print(person) for person in queue]
            queue = []
        else:
            queue.append(line)


solve()
