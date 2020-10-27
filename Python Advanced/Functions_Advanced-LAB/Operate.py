def operate(operator, *args):
    numbers = args
    if operator == '+':
        sum = 0
        for i in range(len(numbers)):
            sum += numbers[i]
    elif operator == '-':
        sum = 0
        for i in range(len(numbers)):
            sum -= numbers[i]
    elif operator == '*':
        sum = 1
        for i in range(len(numbers)):
            sum *= numbers[i]
    elif operator == '/':
        sum = 1
        for i in range(len(numbers)):
            sum /= numbers[i]
    else:
        print('Invalid operator!')

    return sum
