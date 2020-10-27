import math
budget = float(input())
flour_kg = float(input())
milk_per_one_coz = (flour_kg * 1.25) / 4
eggs = flour_kg * 0.75
counter = 1
col_eggs = 0

price_for_one_coz = flour_kg + milk_per_one_coz + eggs
coz_sum = budget / price_for_one_coz
money_left = budget - (price_for_one_coz * math.floor(coz_sum))

for i in range(1, math.floor(coz_sum) + 1):
    if counter % 3 == 0:
        col_eggs = col_eggs - (i - 2)
    col_eggs += 3
    counter += 1


print(f'You made {math.floor(coz_sum)} cozonacs! Now you have {col_eggs} eggs and {money_left:.2f}BGN left.')