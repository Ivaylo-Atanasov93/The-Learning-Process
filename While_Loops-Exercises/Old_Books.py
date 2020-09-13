book = input()
capacity = int(input())
counter = 0
finding = False
founded_book = '00000'

while counter + 1 <= capacity and finding == False:
    founded_book = input()
    counter = counter + 1
    if founded_book == book:
        print(f'You checked {counter - 1} books and found it.')
        finding = True
    elif counter == capacity:
        print('The book you search is not here!')
        print(f'You checked {counter} books.')
        break