def fibonacci():
    numbers = []
    counter = 0
    while True:
        if counter < 2:
            next_num = counter
            numbers.append(next_num)
            counter += 1
        else:
            next_num = numbers[counter - 1] + numbers[counter - 2]
            counter += 1
            numbers.append(next_num)
        yield next_num





generator = fibonacci()
for i in range(20):
    print(next(generator))
