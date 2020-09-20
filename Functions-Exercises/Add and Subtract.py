a = int(input())
b = int(input())
c = int(input())

def sum(a, b):
    return a + b


def subtract(b, c):
    return b - c


def result(a, b, c):
    num_one = sum(a, b)
    result = subtract(num_one, c)
    print(result)


result(a, b, c)


