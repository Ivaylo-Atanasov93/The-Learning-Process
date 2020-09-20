def char_range(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=' ')


symbol_one = input()
symbol_two = input()

char_range(symbol_one, symbol_two)