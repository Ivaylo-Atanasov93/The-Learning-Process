def multiply(*args):
    numbers = args
    sum = 1
    for i in range(len(numbers)):
        sum *= numbers[i]
    return sum
