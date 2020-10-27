number = int(input())
longest = []
for i in range(number):
    (first, second) = input().split('-')
    current_first = first.split(',')
    current_second = second.split(',')

    first_set = set([num for num in range(int(current_first[0]), int(current_first[1]) + 1)])
    second_set = set([num for num in range(int(current_second[0]), int(current_second[1]) + 1)])

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest):
        longest = intersection

print(f'Longest intersection is {list(longest)} with length {len(longest)}')
