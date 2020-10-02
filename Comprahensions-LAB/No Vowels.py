string = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I',]
clear_string = [char for char in string if char not in vowels]
print(''.join(clear_string))