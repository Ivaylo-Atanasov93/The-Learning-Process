def triangle(size):
    for i in range(1, size + 1):
        if i > 1:
            print()
        for j in range(1, i + 1):
            print(j, end=' ')

    for i in range(size -1, 0, -1):
        print()
        for j in range(1, i + 1):
            print(j, end=' ')