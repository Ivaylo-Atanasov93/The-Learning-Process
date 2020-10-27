from fibonacci.fibo_seq_calc import create_sequence, find_the_number


def runner():
    while True:
        command = input()
        if command == 'Stop':
            break
        run = command.split(' ')[0]
        if run == 'Create':
            num = int(command.split(' ')[2])
            create_sequence(num)
        elif run == 'Locate':
            num = int(command.split(' ')[1])
            find_the_number(num)

runner()
