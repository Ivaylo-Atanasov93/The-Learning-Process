number = input().split()
first_set = int(number[0])
second_set = int(number[1])
set_a = set()
set_b = set()
[set_a.add(int(input())) for i in range(first_set)]
[set_b.add(int(input())) for i in range(second_set)]
common = set_a.intersection(set_b)
[print(num) for num in common]