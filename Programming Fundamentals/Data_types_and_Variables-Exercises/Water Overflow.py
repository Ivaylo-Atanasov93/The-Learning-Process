n = int(input())
capacity = 255
intake = 0

for i in range(0, n):
    liters = int(input())
    intake += liters
    if intake > capacity:
        intake = intake - liters
        print('Insufficient capacity!')


print(intake)