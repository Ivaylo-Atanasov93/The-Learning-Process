string = input().split()
shuffle_times = int(input())
shuffled_string = []

for i in range(shuffle_times):
    first_half = string[:int(len(string) / 2)]
    second_half = string[int(len(string) / 2):]
    shuffled_string = []
    for j in range(len(first_half)):
        shuffled_string.append(first_half[j])
        shuffled_string.append(second_half[j])
    string = shuffled_string

print(shuffled_string)

