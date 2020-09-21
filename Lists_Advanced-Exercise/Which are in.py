words = input().split(', ')
string = input()
result = [word for word in words if word in string]
print(result)
