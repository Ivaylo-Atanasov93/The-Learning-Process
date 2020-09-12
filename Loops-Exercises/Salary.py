tabs = int(input())
salary = float(input())

for i in range(0, tabs):
    if salary > 0:
        site = input().lower()
        if site == 'facebook':
            salary = salary - 150
        elif site == 'instagram':
            salary = salary - 100
        elif site == "reddit":
            salary = salary - 50
    else:
        print('You have lost your salary.')
        break


if salary > 0:
    print(round(salary))