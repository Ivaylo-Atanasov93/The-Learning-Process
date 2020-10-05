sequence = []


def create_sequence(number):
    global sequence
    sequence = []
    if number > 1:
        if len(sequence) < 2:
            sequence.append(0)
            sequence.append(1)
        for i in range(2, number):
            sequence.append(sequence[i - 1] + sequence[i - 2])
    elif number == 1:
        sequence.append(0)
        sequence.append(1)
    else:
        sequence.append(0)
    print(sequence)


def find_the_number(number):
    global sequence
    if number in sequence:
        print(f'The number - {number} is at index {sequence.index(number)}')
    else:
        print(f'The number {number} is not in the sequence')
