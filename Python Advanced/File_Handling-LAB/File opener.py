file_path = './Files/text.txt'

try:
    open(file_path, 'r')
    print('File found')
except:
    print('File not found')
