def even_odd(*args):
    args = list(args)
    command = args.pop()
    print(command)
    if command == 'even':
        return [num for num in args if num % 2 == 0]
    elif command == 'odd':
        return [num for num in args if num % 2 != 0]
    else:
        return 'Invalid command!'


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))