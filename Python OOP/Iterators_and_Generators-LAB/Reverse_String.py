def reverse_text(text):
    text = text[::-1]
    for i in range(len(text)):
        yield text[i]


for char in reverse_text("step"):
    print(char, end='')
