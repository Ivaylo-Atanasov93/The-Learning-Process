def odd(numbers):
    return sum([num for num in numbers if num % 2 != 0])


def even(numbers):
    return sum([num for num in numbers if num % 2 == 0])


command = input()
numbers = [int(num) for num in input().split()]

if command == 'Odd':
    print(odd(numbers) * len(numbers))
elif command == 'Even':
    print(even(numbers) * len(numbers))
