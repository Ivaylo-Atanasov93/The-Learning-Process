file_path = './Files/numbers.txt'
file = open(file_path)
numbers = []
for line in file:
    #line = line.strip()    #If there is a new lines in the file
    if line != '':
        numbers.append(int(line))

print(sum(numbers))