words = {}

while True:
    string = input()
    if string == 'end':
        break
    words[string] = string[::-1]

for key in words:
    print(f'{key} = {words[key]}')
