import re
numbers = input()
regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
accurate_numbers = re.finditer(regex, numbers)
for number in accurate_numbers:
    print(number.group(0), end=' ')