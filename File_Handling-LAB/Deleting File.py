from os import remove
from os.path import exists

file_path = './Files/to_write.txt'

if exists(file_path):
    remove(file_path)
else:
    print('File already deleted')

try:
    remove(file_path)
except FileNotFoundError:
    print('File already deleted')

