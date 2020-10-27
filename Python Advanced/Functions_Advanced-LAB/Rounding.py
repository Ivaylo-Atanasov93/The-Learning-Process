def absolute_values(string):
    numbers = string.split()
    numbers = [round(float(x)) for x in numbers]
    return numbers


print(absolute_values(input()))
