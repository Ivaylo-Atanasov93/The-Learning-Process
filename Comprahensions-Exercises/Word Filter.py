string = input().split()
[print(word) for word in string if len(word) % 2 == 0]