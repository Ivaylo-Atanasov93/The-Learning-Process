string = input().split('.')
string = int(''.join(string))
string += 1
string = list(map(int, str(string)))
print(f'{string[0]}.{string[1]}.{string[2]}')