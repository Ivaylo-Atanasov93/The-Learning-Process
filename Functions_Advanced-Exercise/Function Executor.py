def func_executor(*args):
    result = []
    for argument in args:
        func = argument[0]
        arguments = argument[1]
        result.append(func(*arguments))

    return result


# def func_executor1(*args):
#     result = []
#     for element in args:
#         func_name = element[0]
#         func_input = element[1]
#         result.append(func_name(*func_input))
#     return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
# print(func_executor1((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
