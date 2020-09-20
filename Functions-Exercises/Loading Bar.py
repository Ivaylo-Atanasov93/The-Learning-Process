def loading_bar(percentage):
    numbers_of_bars = int(int(percentage) / 10)
    loading_bar = []

    for i in range(numbers_of_bars):
        loading_bar.append('%')

    for i in range(10 - numbers_of_bars):
        loading_bar.append('.')
    if numbers_of_bars == 10:
        print('100% Complete!')
        print('[', end='')
        for i in loading_bar:
            print(i, end='')
        print(']')

    if numbers_of_bars < 10:
        print(f'{percentage}% [', end='')
        for i in loading_bar:
            print(i, end='')
        print(']')
        print('Still loading...')


percentage = input()
loading_bar(percentage)
