from collections import defaultdict
words = input().lower().split()
occurrences = defaultdict(int)
for word in words:
    occurrences[word] += 1

for word in occurrences:
    if occurrences[word] % 2 != 0:
        print(word, end=' ')