fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0
current_fire = []
extinguished_fires = []


for i in range(len(fires)):
    current_fire = fires[i].split(' = ')
    if water - int(current_fire[1]) < 0:
        break

    if current_fire[0] == 'High' and 80 < int(current_fire[1]) <= 125:
        water -= int(current_fire[1])
        total_fire += int(current_fire[1])
        extinguished_fires.append(current_fire[1])
        effort += int(current_fire[1]) * 0.25

    elif current_fire[0] == 'Medium' and 50 < int(current_fire[1]) <= 80:
        water -= int(current_fire[1])
        total_fire += int(current_fire[1])
        extinguished_fires.append(current_fire[1])
        effort += int(current_fire[1]) * 0.25

    elif current_fire[0] == 'Low' and 0 < int(current_fire[1]) <= 50:
        water -= int(current_fire[1])
        total_fire += int(current_fire[1])
        extinguished_fires.append(current_fire[1])
        effort += int(current_fire[1]) * 0.25

    else:
        continue

print('Cells:')
for i in range(len(extinguished_fires)):
    print(f'- {extinguished_fires[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total fire: {total_fire}')