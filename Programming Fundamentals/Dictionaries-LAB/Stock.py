line = input().split()
revision = {}
for i in range(0, len(line), 2):
    key = line[i]
    value = line[i + 1]
    revision[key] = int(value)

check_products = input().split()
for product in check_products:
    if product in revision:
        print(f'We have {revision[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")