budget = float(input())
season = input()

percentage = 1
destination = ''
place_for_sleep = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        percentage = percentage * 0.3
        place_for_sleep = 'Camp'
    elif season == 'winter':
        percentage = percentage * 0.7
        place_for_sleep = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        percentage = percentage * 0.4
        place_for_sleep = 'Camp'
    elif season == 'winter':
        percentage = percentage * 0.8
        place_for_sleep = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    percentage = percentage * 0.9
    place_for_sleep = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place_for_sleep} - {budget * percentage:.2f}')