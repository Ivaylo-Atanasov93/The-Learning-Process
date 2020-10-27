def rhombus(number):
    for i in range(number + 1):
        print(' ' * (number - i), '* ' * i)
    for i in range(number - 1, -1, -1):
        print(' ' * (number - i), '* ' * i)


rhombus(int(input()))