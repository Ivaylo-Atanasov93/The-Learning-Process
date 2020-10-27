persons = int(input())
capacity = int(input())
counter = 0

for i in range(0, persons, capacity):
    counter += 1

print(counter)