import re

text = input()#.lower()
word = input()#.lower()
word = '\\b'+word+'\\b'

x = re.findall(word, text, re.IGNORECASE)
print(len(x))