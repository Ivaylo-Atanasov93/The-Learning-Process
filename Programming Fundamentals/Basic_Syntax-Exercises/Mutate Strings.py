string_one = input()
string_two = input()
position = 0

for i in range(0, len(string_one)):
    if string_one[position] != string_two[position]:
        print(string_two[:position+1], end='')
        print(string_one[position+1:])
        position += 1
    else:
        position += 1