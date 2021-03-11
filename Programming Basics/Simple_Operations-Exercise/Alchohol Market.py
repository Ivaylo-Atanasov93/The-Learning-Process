# whiskey_price_perL = float(input())
# beer_liters = float(input())
# wine_liters = float(input())
# rakia_liters = float(input())
# whiskey_liters = float(input())
#
# rakia_price_perL = whiskey_price_perL * 0.5
# wine_price_perL = rakia_price_perL * 0.6
# beer_price_perL = rakia_price_perL * 0.2
#
# final_rakia_price = rakia_price_perL * rakia_liters
# final_wine_price = wine_price_perL * wine_liters
# final_beer_price = beer_price_perL * beer_liters
# final_whiskey_price = whiskey_price_perL * whiskey_liters
#
# sum = final_beer_price + final_rakia_price + final_whiskey_price + final_wine_price
# print(f'{sum:.2f}')

string = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2484.3372319336086!2d-0.025307634343760214!3d51.488678729632035!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x48760293562d4569%3A0x47e70eaa4c4f437e!2sMaritime%20Quay%2C%20Isle%20of%20Dogs%2C%20London%20E14%203QH!5e0!3m2!1sen!2suk!4v1614365837185!5m2!1sen!2suk" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'
location = string.split('"')
print(location[1])