word = input()
letter = ''
for i in range(len(word) - 1, -1, -1):
    letter += word[i]

print(letter)
