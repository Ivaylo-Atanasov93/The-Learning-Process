width = int(input())
length = int(input())

cake = width * length
cake_left = 0
pieces = ''
done = False

while cake > 0 and done == False:
    pieces = input()
    if pieces == 'STOP':
        done = True
        break

    pieces = int(pieces)
    cake = cake - pieces

if cake < 0:
    print(f'No more cake left! You need {abs(cake)} pieces more.')
else:
    print(f'{cake} pieces are left.')