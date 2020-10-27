string = input()
digits = ''
letters = ''
other = ''

for symbol in string:
    if 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
        letters += symbol
    elif 48 <= ord(symbol) <= 57:
        digits += symbol
    else:
        other += symbol

print(digits)
print(letters)
print(other)