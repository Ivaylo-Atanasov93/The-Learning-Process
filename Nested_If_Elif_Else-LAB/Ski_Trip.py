days = int(input())
room = input()
rating = input()

price_of_the_trip = 0
bill = 0

if room == 'apartment':
    if days <= 10:
        bill = 25 * 0.7
    elif days <= 15:
        bill = 25 * 0.65
    else:
        bill = 25 * 0.5

elif room == 'president apartment':
    if days <= 10:
        bill = 35 * 0.9
    elif days <= 15:
        bill = 35 * 0.85
    else:
        bill = 35 * 0.8

elif room == 'room for one person':
        bill = 18

price_of_the_trip = bill * (days - 1)


if rating == 'positive':
    price_of_the_trip = price_of_the_trip * 1.25
elif rating == 'negative':
    price_of_the_trip = price_of_the_trip * 0.9

print(f'{price_of_the_trip:.2f}')
