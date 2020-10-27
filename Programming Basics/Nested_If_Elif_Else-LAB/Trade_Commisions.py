town = input()
sales = float(input())

commission_rate = 0

if town == 'Sofia':
    if 0 <= sales <= 500:
        commission_rate = commission_rate + 0.05
    elif 500 < sales <= 1000:
        commission_rate = commission_rate + 0.07
    elif 1000 < sales <= 10000:
        commission_rate = commission_rate + 0.08
    elif sales > 10000:
        commission_rate = commission_rate + 0.12
    else: print('error')
elif town == 'Varna':
    if 0 <= sales <= 500:
        commission_rate = commission_rate + 0.045
    elif 500 < sales <= 1000:
        commission_rate = commission_rate + 0.075
    elif 1000 < sales <= 10000:
        commission_rate = commission_rate + 0.1
    elif sales > 10000:
        commission_rate = commission_rate + 0.13
    else: print('error')
elif town == 'Plovdiv':
    if 0 <= sales <=500:
        commission_rate = commission_rate + 0.055
    elif 500 < sales <= 1000:
        commission_rate = commission_rate + 0.08
    elif 1000 < sales <= 10000:
        commission_rate = commission_rate + 0.12
    elif sales > 10000:
        commission_rate = commission_rate + 0.145
    else: print('error')
else: print('error')

if commission_rate > 0:
    print(f'{sales * commission_rate:.2f}')
    