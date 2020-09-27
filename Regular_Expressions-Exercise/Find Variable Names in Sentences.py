import re

pattern = r'\b(_)([A-Za-z0-9]+\b)'
text = input()

matches = re.findall(pattern, text)
variable_names = []

for match in matches:
    variable_names.append(match[1])

print(','.join(variable_names))






# import re
# string = input()
# regex = r'(?<=_)[A-Za-z0-9]+(?=\s)'
# variables = re.findall(regex, string)
# print(','.join(variables))