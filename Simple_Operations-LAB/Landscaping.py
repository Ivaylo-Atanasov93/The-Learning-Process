square_meters = float(input('Enter the square meters of the yards: '))
price = 7.61
discount = float(input('Enter the discount percentages: '))
calculated_discount = 100 - discount
finalPrice = (square_meters * price) * (calculated_discount / 100)
theDiscount = (square_meters * price) - finalPrice
print(f'The final price is: {finalPrice:.2f} lv.')
print(f'The discount is: {theDiscount:.2f}')