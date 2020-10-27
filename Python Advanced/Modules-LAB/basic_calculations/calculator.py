def calculate(string):
    num_1 = float(string.split(' ')[0])
    num_2 = int(string.split(' ')[2])
    operator = string.split(' ')[1]
    result = 0
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    elif operator == '/':
        result = num_1 / num_2
    elif operator == '^':
        result = num_1 ** num_2
    else:
        print('Invalid operator!')

    print(f'{result:.2f}')