import re

def get_words_from_file(file_path):
    with open(words_file_path, 'r') as file:
        return file.read().split()


def get_words_count(file_path, words):
    words_count = {word: 0 for word in words}

    with open(file_path, 'r') as input_file:
        for line in input_file:
            words_in_line = re.findall(r'[A-Za-z0-9]+', line.lower(), re.IGNORECASE)
            for word in words:
                words_count[word] += words_in_line.count(word)
    return words_count


input_file_path = './Files/input.txt'
words_file_path = './Files/words.txt'
print(get_words_count(input_file_path, get_words_from_file(words_file_path)))

# def get_words():
#     with open(words_file_path, 'r') as words_file:
#         return words_file.read().split()
#
#
# def count_words():
#     with open(input_file_path, 'r') as input_file:
#         for line in input_file:
#             for word in get_words():
#                 if word in line.lower():
#                     counter[word] += 1
#
#
# count_words()
# counter = {k: v for k, v in sorted(counter.items(), key=lambda item: -item[1])}
# [print(f'{key} - {value}') for key, value in counter.items()]
