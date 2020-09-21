import matplotlib.pyplot as plt

annual_return = float(input('What % of return you are expecting per year?: ')) / 100
years = int(input('How many years you think that you will hold these shares?: '))
starting_capital = float(input('With what amount of money you are going to start?: '))
increase_per_year = []
initial_capital = starting_capital
duration = []

for year in range(years):
    initial_capital += (initial_capital * annual_return)
    increase_per_year.append(initial_capital)
    duration.append(year + 1)
    print(f'Your initial capital is increased to: {initial_capital:.2f}')

percentage = (initial_capital / starting_capital) * 100
plt.plot(duration, increase_per_year, label='Increase curve.')
plt.xlabel('Investing period')
plt.ylabel('Increasing per year')
plt.title(f'Your return for {years} years will be ${initial_capital:.2f} or {percentage:.2f}%.')
plt.legend()
plt.show()