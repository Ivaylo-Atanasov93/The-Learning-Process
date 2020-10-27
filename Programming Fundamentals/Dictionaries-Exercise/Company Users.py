from collections import defaultdict

companies = defaultdict(list)
end = False

while not end:
    line = input().split(" -> ")
    if line[0] == 'End':
        end = True
        break
    company = line[0]
    employee = line[1]
    if employee in companies[company]:
        continue
    companies[company].append(employee)

companies = dict(sorted(companies.items()))

for company in companies:
    print(f'{company}')
    for employee in companies[company]:
        print(f'-- {employee}')