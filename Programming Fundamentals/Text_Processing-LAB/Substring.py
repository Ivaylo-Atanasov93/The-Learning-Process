word = input()
string = input()

while word in string:
    string = string.replace(word, '')
print(string)