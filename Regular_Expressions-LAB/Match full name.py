import re
string = input()
regex = r'(\\b[A-Z][a-z]+\s[A-Z][a-z]+\\b)'
correct_string = re.findall(regex, string)
print(' '.join(correct_string))
