string = input()
emoticons = []
for i in range(len(string)):
    if string[i] == ':':
        emoticon = string[i] + string[i + 1]
        emoticons.append(emoticon)

for emoticon in emoticons:
    print(emoticon)
