import fileinput
from os import remove
from os.path import exists


def create(file_path):
    with open(file_path, 'w') as file:
        return file


def add(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content + '\n')
        return


def replace_string(file_path, old_content, new_content):
    if exists(file_path):
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                print(line.replace(old_content, new_content), end='')
    else:
        print('An error occurred')
        return


def delete(file_path):
    if exists(file_path):
        remove(file_path)
        return
    else:
        print('An error occurred')


def command_receiver():

    while True:
        command = input().split('-')
        if command[0] == 'End':
            break

        elif len(command) <= 1:
            print('Invalid command!')

        else:
            file_path = './Files/Task_3/' + command[1]

            if command[0] == 'Create':
                create(file_path)

            elif command[0] == 'Add':
                content = command[2]
                add(file_path, content)

            elif command[0] == 'Replace':
                old_content = command[2]
                new_content = command[3]
                replace_string(file_path, old_content, new_content)

            elif command[0] == 'Delete':
                delete(file_path)


command_receiver()
