string = input().split()
happiness_factor = int(input())
all_employees_happiness = [int(employee) for employee in string]
employees = list(map(lambda x: int(x) * happiness_factor, all_employees_happiness))
greater_happiness_employees = list(filter(lambda x: x >= sum(employees) / len(employees), employees))

if len(greater_happiness_employees) >= len(employees) / 2:
    print(f'Score: {len(greater_happiness_employees)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(greater_happiness_employees)}/{len(employees)}. Employees are not happy!')