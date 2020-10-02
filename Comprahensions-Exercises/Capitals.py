countries = [country for country in input().split(', ')]
capitals = [capital for capital in input().split(', ')]
[print(f'{countries[i]} -> {capitals[i]}') for i in range(len(countries))]