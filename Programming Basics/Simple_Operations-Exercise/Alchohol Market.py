whiskey_price_perL = float(input())
beer_liters = float(input())
wine_liters = float(input())
rakia_liters = float(input())
whiskey_liters = float(input())

rakia_price_perL = whiskey_price_perL * 0.5
wine_price_perL = rakia_price_perL * 0.6
beer_price_perL = rakia_price_perL * 0.2

final_rakia_price = rakia_price_perL * rakia_liters
final_wine_price = wine_price_perL * wine_liters
final_beer_price = beer_price_perL * beer_liters
final_whiskey_price = whiskey_price_perL * whiskey_liters

sum = final_beer_price + final_rakia_price + final_whiskey_price + final_wine_price
print(f'{sum:.2f}')