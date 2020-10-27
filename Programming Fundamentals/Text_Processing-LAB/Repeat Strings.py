string = input().split()
result = ''

for element in string:
    result += element * len(element)

print(result)