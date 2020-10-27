from collections import defaultdict

text = input().replace(' ','')
dictionary = defaultdict(int)
for i in text:
    dictionary[i] += 1

for letter in dictionary:
    print(f'{letter} -> {dictionary[letter]}')
