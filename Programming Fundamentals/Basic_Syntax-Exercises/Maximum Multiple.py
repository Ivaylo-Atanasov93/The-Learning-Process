devisor = int(input())
bound = int(input())
greater_number = 0
for i in range(1, bound + 1):
    if i % devisor == 0:
        greater_number = i

print(greater_number)