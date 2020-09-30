number = int(input())
unique_elements = set()
for i in range(number):
    elements = input().split()
    [unique_elements.add(element) for element in elements]

[print(element) for element in unique_elements]
