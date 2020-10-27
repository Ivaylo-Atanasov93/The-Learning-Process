centuries = int(input())
years = centuries * 100
days = years * 365.2422
hours = int(days) * 24
minutes = int(hours) * 60

print(f'{centuries} centuries = {years} years = {int(days)} days = {int(hours)} hours = {int(minutes)} minutes')