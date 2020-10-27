def absolute_values(string):
    numbers = string.split()
    numbers = [abs(float(x)) for x in numbers]
    return numbers


print(absolute_values(input()))
