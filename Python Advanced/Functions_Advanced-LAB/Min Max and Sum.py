def min_num(numbers):
    min_num = min(numbers)
    return min_num


def max_num(numbers):
    max_num = max(numbers)
    return max_num


def num_sum(numbers):
    num_sum = sum(numbers)
    return num_sum


numbers = [int(x) for x in input().split()]
print(f'The minimum number is {min_num(numbers)}')
print(f'The maximum number is {max_num(numbers)}')
print(f'The sum number is: {num_sum(numbers)}')