import re

regex = r'(\d+)'


while True:
    string = input()
    if string != '':
        numbers = re.findall(regex, string)
        for num in numbers:
            print(num, end=' ')
    else:
        break