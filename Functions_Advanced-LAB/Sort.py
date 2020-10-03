def sorted_numbers(numbers):
    numbers = [int(x) for x in numbers]
    return sorted(numbers)

print(sorted_numbers(input().split()))