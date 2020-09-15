n = float(input())

if n == 0:
    print('zero')
elif -1 < n < 0:
    print('small negative')
elif 0 < n < 1:
    print('small positive')
elif -1000000 < n <= -1:
    print('negative')
elif n < - 1000000:
    print('large negative')
elif 1 < n < 1000000:
    print('positive')
elif n > 1000000:
    print('large positive')