file_path = './Files/to_write.txt'
file = open(file_path, 'w')
file.write('This is my first file. Reached time from the lecture: 1:00:00 \n')
file.close()

with open(file_path, 'a') as file:
    file.write('This is my second line of my first file created by the program that i wrote.')

