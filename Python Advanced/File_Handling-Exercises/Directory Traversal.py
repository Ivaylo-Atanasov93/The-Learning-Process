import os
from collections import defaultdict

file_path = input()
deepnes = file_path.count('\\')
files_list = defaultdict(list)
username = os.getlogin()

for root, dirs, files in os.walk(file_path):
    for file in files:
        # TODO Condition for going only into one directory deepness.
        if str(root).count('\\') <= deepnes + 1:
            type = f'.{file.split(".")[1]}'
            files_list[type].append(file)

desktop_path = f'C:\\Users\\{username}\\Desktop\\report.txt'

with open(desktop_path, 'w') as report:


    for key, value in sorted(files_list.items()):
        report.write(f'{key}\n')
        for item in value:
            report.write(f'- - - {item}\n')