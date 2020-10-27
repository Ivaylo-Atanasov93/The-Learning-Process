word = input()
num = len(word)
sum = 0
for i in range(0, num):
    if word[i] == 'a':
        sum = sum + 1
    elif word[i] == 'e':
        sum = sum + 2
    elif word[i] == 'i':
        sum = sum + 3
    elif word[i] == 'o':
        sum = sum + 4
    elif word[i] == 'u':
        sum = sum + 5

print(sum)