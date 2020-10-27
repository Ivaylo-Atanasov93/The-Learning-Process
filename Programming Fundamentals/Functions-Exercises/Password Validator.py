def pasword_validator(password):
    required_symbols = True
    digit_counter = 0
    checkers = 0
    usable_symbols = []
    for i in range(48, 58):                         # importing the legal characters from ASCII
        usable_symbols.append(chr(i))
    for i in range(65, 91):
        usable_symbols.append(chr(i))
    for i in range(97, 123):
        usable_symbols.append(chr(i))

    for i in password:                              # checking for legal characters
        if i not in usable_symbols:
            print('Password must consist only of letters and digits')
            required_symbols = False
            break
    if required_symbols:
        checkers += 1

    if 6 <= len(password) <= 10:                    # checking for legal lenght
        checkers += 1
    else:
        print('Password must be between 6 and 10 characters')

    for i in password:                              #checking for required number of digits
        if i in usable_symbols[0:9]:
            digit_counter += 1
    if digit_counter >= 2:
        checkers += 1
    else:
        print('Password must have at least 2 digits')


    if checkers == 3:                               # final check for every requirement
        print('Password is valid')



password = input()
pasword_validator(password)
