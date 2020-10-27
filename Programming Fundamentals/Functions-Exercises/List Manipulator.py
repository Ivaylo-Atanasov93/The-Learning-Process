import sys


def exchange(string):                                          # _____________ EXCHANGE SECTION _______________
    if int(splitted_command[1]) < 0 or int(splitted_command[1]) > len(string) - 1:
        print('Invalid index')
    else:
        array = []
        for i in range(int(splitted_command[1]) + 1, len(string)):
            array.append(string[i])
        for i in range(int(splitted_command[1]) + 1):
            array.append(string[i])
        string.clear()
        for i in range(len(array)):
            string.append(array[i])


def max_odd(string):                                            # ________________ MAX SECTION _________________
    max_num = -sys.maxsize
    max_num_index = -1
    for i in range(len(string)):
        if string[i] % 2 != 0 and string[i] >= max_num:
            max_num = string[i]
            max_num_index = i
    if max_num_index != -1:
        print(max_num_index)
    else:
        print('No matches')


def max_even(string):
    max_num = -sys.maxsize
    max_num_index = -1
    for i in range(len(string)):
        if string[i] % 2 == 0 and string[i] >= max_num:
            max_num = string[i]
            max_num_index = i
    if max_num_index != -1:
        print(max_num_index)
    else:
        print('No matches')


def min_odd(string):                                             # ________________ MIN SECTION _________________
    min_num = sys.maxsize
    min_num_index = -1
    for i in range(len(string)):
        if string[i] % 2 != 0 and string[i] <= min_num:
            min_num = string[i]
            min_num_index = i
    if min_num_index != -1:
        print(min_num_index)
    else:
        print('No matches')


def min_even(string):
    min_num = sys.maxsize
    min_num_index = -1
    for i in range(len(string)):
        if string[i] % 2 == 0 and string[i] <= min_num:
            min_num = string[i]
            min_num_index = i
    if min_num_index != -1:
        print(min_num_index)
    else:
        print('No matches')


def first_even_counter(string):                                   # _______________ FIRST SECTION ________________
    array_count = []
    for i in range(int(len(string))):
        if int(string[i]) % 2 == 0:
            array_count.append(int(string[i]))
    if len(string) < int(splitted_command[1]):
        print('Invalid count')
    else:
        print(array_count[:int(splitted_command[1])])


def first_odd_counter(string):
    array_count = []
    for i in range(int(len(string))):
        if int(string[i]) % 2 != 0:
            array_count.append(int(string[i]))
    if len(string) < int(splitted_command[1]):
        print('Invalid count')
    else:
        print(array_count[:int(splitted_command[1])])


def last_even_counter(string):                                     # _______________ LAST SECTION ________________
    array_count = []
    for i in range(int(len(string))):
        if int(string[i]) % 2 == 0:
            array_count.append(int(string[i]))
    if len(string) < int(splitted_command[1]):
        print('Invalid count')
    else:
        print(array_count[-int(splitted_command[1]):])


def last_odd_counter(string):
    array_count = []
    for i in range(int(len(string))):
        if int(string[i]) % 2 != 0:
            array_count.append(int(string[i]))
    if len(string) < int(splitted_command[1]):
        print('Invalid count')
    else:
        print(array_count[-int(splitted_command[1]):])


string = input().split(' ')
for i in range(len(string)):
    string[i] = int(string[i])
command = ''

while command != 'end':

    command = input()
    splitted_command = command.split(' ')

    if splitted_command[0] == 'end':
        print(string)
        break

    elif splitted_command[0] == 'exchange':
        exchange(string)

    elif splitted_command[0] == 'max':
        if splitted_command[1] == 'even':
            max_even(string)
        elif splitted_command[1] == 'odd':
            max_odd(string)

    elif splitted_command[0] == 'min':
        if splitted_command[1] == 'even':
            min_even(string)
        elif splitted_command[1] == 'odd':
            min_odd(string)

    elif splitted_command[0] == 'first':
        if splitted_command[2] == 'even':
            first_even_counter(string)
        elif splitted_command[2] == 'odd':
            first_odd_counter(string)

    elif splitted_command[0] == 'last':
        if splitted_command[2] == 'even':
            last_even_counter(string)
        elif splitted_command[2] == 'odd':
            last_odd_counter(string)