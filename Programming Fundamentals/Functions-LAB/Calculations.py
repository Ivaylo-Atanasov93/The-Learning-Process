operation = input()
x = int(input())
y = int(input())

def basic_calculator(x, y, operation):
    if operation == 'multiply':
        return x * y
    elif operation == 'divide':
        return x // y
    elif operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y

print(basic_calculator(x, y, operation))