string = input().split(', ')
beggars = int(input())
beggars_list = []
for _ in range(beggars):
    beggars_list.append(0)

for i in range(len(string)):
    current = i % beggars
    beggars_list[current] = beggars_list[current] + int(string[i])
print(beggars_list)