n = int(input())
sum_of_chars = 0
for i in range(0, n):
    char = input()
    sum_of_chars += ord(char)

print(f'The sum equals: {sum_of_chars}')