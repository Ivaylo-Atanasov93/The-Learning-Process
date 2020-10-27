string = input().split()
remove = int(input())

for i in range(len(string)):
    string[i] = int(string[i])

for _ in range(remove):
    string.remove(min(string))

print(string)