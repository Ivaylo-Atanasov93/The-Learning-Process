def read_next(*args):
    for item in args:
        for symbol in item:
            yield symbol


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}, [1, 2, 3, 10, 15]):
    print(item, end='')
