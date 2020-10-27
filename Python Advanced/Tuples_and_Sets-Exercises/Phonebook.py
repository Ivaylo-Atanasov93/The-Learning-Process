phone_book = {}
string = ''

while len(string) != 1:
    string = input().split('-')
    if len(string) != 1:
        phone_book[string[0]] = string[1]
    else:
        string = int(string[0])
        break

for i in range(string):
    name = input()
    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')
