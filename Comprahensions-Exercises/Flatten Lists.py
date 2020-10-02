line = input()
result = [el for x in line.split('|')[::-1] for el in x.split() if el != '']
print(' '.join(result))

string = input().split("|")
result = []
string = [[result.append(symbol.strip()) for symbol in element if symbol.strip() != ''] for element in string[::-1]]
print(' '.join(result))

string = input().split('|')
string = [element.replace(' ', '') for element in string]
string = string[::-1]
[print(' '.join(element), end=' ') for element in string]
