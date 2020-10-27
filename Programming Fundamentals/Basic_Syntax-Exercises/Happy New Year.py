year = input()
happy = False


while not happy:
    year = int(year)
    year += 1
    year = str(year)
    unique_count = len(set(year))
    if unique_count == len(year):
        happy = True
        break




print(year)
