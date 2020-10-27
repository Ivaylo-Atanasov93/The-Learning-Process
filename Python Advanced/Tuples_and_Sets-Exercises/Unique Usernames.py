that_much = int(input())
usernames = set()
[usernames.add(input()) for i in range(that_much)]
[print(username) for username in usernames]
