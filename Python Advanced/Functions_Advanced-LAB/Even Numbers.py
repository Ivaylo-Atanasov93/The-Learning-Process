def filtering(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def absolute_values(string):
    numbers = string.split()
    numbers = [int(x) for x in numbers]
    return filtering(numbers)


print(absolute_values(input()))
