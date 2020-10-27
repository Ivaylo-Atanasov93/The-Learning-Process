import shutil


def text_writter(line, counts, index):
    letter_counts, punkt_counts = counts
    text = f'Line {index}: {line} ({letter_counts})({punkt_counts})'
    with open('output.txt', 'a') as file:
        file.write(text + '\n')
    return


def line_checker(line):
    letter_counter = 0
    punct_marks = 0
    for symbol in line:
        if symbol.isalpha():
            letter_counter += 1
        elif symbol != ' ' and not symbol.isalpha():
            punct_marks += 1
    return (letter_counter, punct_marks)


def file_reader(file, index=1):
    for line in file:
        line = line.strip()
        text_writter(line, line_checker(line), index)
        index += 1


file_path = './Files/text.txt'
file = open(file_path, 'r')
file_reader(file)
shutil.move('./output.txt', './Files/output.txt')
