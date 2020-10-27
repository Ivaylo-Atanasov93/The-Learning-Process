month = input()
nights = int(input())

price_per_night_studio = 0
price_per_night_apartment = 0
studio_discount = 1
apartment_discount = 1

if month == 'May' or month == 'October':
    price_per_night_studio = price_per_night_studio + 50
    price_per_night_apartment = price_per_night_apartment + 65
    if nights > 14:
        studio_discount = studio_discount * 0.70
        apartment_discount = apartment_discount * 0.90
    elif nights > 7:
        studio_discount = studio_discount * 0.95

elif month == 'June' or month == 'September':
    price_per_night_studio = price_per_night_studio + 75.20
    price_per_night_apartment = price_per_night_apartment + 68.70
    if nights > 14:
        studio_discount = studio_discount * 0.80
        apartment_discount = apartment_discount * 0.90

elif month == 'July' or month == 'August':
    price_per_night_studio = price_per_night_studio + 76
    price_per_night_apartment = price_per_night_apartment + 77
    if nights > 14:
        apartment_discount = apartment_discount * 0.90

final_price_studio = (price_per_night_studio * nights) * studio_discount
final_price_apartment = (price_per_night_apartment * nights) * apartment_discount

print(f'Apartment: {final_price_apartment:.2f} lv.')
print(f'Studio: {final_price_studio:.2f} lv.')