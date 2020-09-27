import re

string = input()
regex = r'((((?<=\s)[a-z-]+)|((?<=\s)[a-z]+[\.\|-|_][a-z]+))@(([a-z]+.[a-z]+)|([a-z]+-[a-z]+\.[a-z]+))\.[a-z]+)'

valid_emails = re.findall(regex, string)
emails = []

for mail in valid_emails:
    print(mail[0])


#regex = r'(((?<=\s)[a-z-]+)|((?<=\s)[a-z]+[\.\|-|_][a-z]+))@'
#regex = r'((((?<=\s)[a-z-]+)|((?<=\s)[a-z]+[\.\|-|_][a-z]+))@(([a-z]+.[a-z]+)|([a-z]+-[a-z]+\.[a-z]+))\.[a-z]+)'
#_\-\.