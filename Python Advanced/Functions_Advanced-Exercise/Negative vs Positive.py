def result(numbers):
    negative = [number for number in numbers if number < 0]
    positive = [number for number in numbers if number >= 0]
    print(sum(negative))
    print(sum(positive))
    if abs(sum(negative)) > sum(positive):
        return print('The negatives are stronger than the positives')
    else:
        return print('The positives are stronger than the negatives')


numbers = [int(x) for x in input().split()]
result(numbers)
