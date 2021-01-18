def reverse_text(string):
    for i in range(1, len(string) + 1):
        yield string[-i]

for char in reverse_text("step"):
    print(char, end='')
