from collections import defaultdict
number = int(input())
dictionary = defaultdict(list)
for i in range(number):
    word = input()
    synonym = input()
    if word in dictionary:
        dictionary[word].append(synonym)
    else:
        dictionary[word].append(synonym)

for word in dictionary:
    print(f'{word} - {", ".join(dictionary[word])}')