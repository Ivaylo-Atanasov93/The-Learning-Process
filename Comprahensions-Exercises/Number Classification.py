numbers = [int(number) for number in input().split(', ')]
positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]
even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]
print(f'Positive: {str(positive).strip("[]")}')
print(f'Negative: {str(negative).strip("[]")}')
print(f'Even: {str(even).strip("[]")}')
print(f'Odd: {str(odd).strip("[]")}')