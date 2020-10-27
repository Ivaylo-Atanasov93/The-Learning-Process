string = input().split(', ')
checkers = 0

usable_symbols = ['-', '_']
for i in range(48, 58):  # importing the legal characters from ASCII
    usable_symbols.append(chr(i))
for i in range(65, 91):
    usable_symbols.append(chr(i))
for i in range(97, 123):
    usable_symbols.append(chr(i))

for username in string:
    checkers = 0
    for char in username:
        if char not in usable_symbols:
            break
        checkers += 1
        if 3 < len(username) < 16 and checkers == len(username):
            print(username)
            break
