def factorial_calculator(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial


def factorial_dividing(a, b):
    a = (factorial_calculator(number_one))
    b = (factorial_calculator(number_two))
    result = a / b
    print(f'{result:.2f}')


number_one = int(input())
number_two = int(input())
factorial_dividing(number_one, number_two)