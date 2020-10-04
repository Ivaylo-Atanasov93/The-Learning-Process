def checking_symbols(line):
    for symbol in line:
        if symbol in symbols:
            line = line.replace(symbol, '@')
    line = line.split()
    result = line[::-1]
    result = ' '.join(result)
    return result


def read_the_file(file, index=1):
    for line in file:
        if index % 2 != 0:
            print(checking_symbols(line))
        index += 1


file_path = './Files/text.txt'
file = open(file_path, 'r')
symbols = ["-", ",", ".", "!", "?"]

read_the_file(file)
