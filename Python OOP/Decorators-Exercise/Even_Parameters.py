def even_parameters(func):
    def wrapper(*args):
        nums = [num for num in args if isinstance(num, int)]
        if len(nums) == len(args):
            even_nums = [num for num in args if num % 2 == 0]
            if len(even_nums) == len(args):
                return func(*args)
        return 'Please use only even numbers!'

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
print()


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
