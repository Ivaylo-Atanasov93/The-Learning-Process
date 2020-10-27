import math
change = float(input())
coins = 0
while change != 0:

    if change > 3:
        coins = change / 2
        coins = math.floor(coins)
        change = change - (math.floor(coins) * 2)
    if 2 <= change < 3:
        change = change % 2
        change = round(change, 2)
        coins = coins + 1
    if change >= 1:
        change = change % 1
        change = round(change, 2)
        coins = coins + 1
    if change >= 0.50:
        change = change % 0.50
        change = round(change, 2)
        coins = coins + 1
    if change >= 0.40:
        change = change % 0.40
        change = round(change, 2)
        coins = coins + 2
    if change >= 0.30:
        change = change % 0.30
        change = round(change, 2)
        coins = coins + 2
    if change >= 0.20:
        change = change % 0.20
        change = round(change, 2)
        coins = coins + 1
    if change >= 0.10:
        change = change % 0.10
        change = round(change, 2)
        coins = coins + 1
    if change >= 0.05:
        change = change % 0.05
        change = round(change, 2)
        coins = coins + 1
    if change >= 0.04:
        change = change % 0.04
        change = round(change, 2)
        coins = coins + 2
    if change >= 0.02:
        change = change % 0.02
        change = round(change, 2)
        coins = coins + 1
    if change >= 0.01:
        change = change % 0.01
        change = round(change, 2)
        coins = coins + 1

print(coins)