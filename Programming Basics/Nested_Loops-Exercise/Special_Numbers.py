n = int(input())
xxx = 0
current_number = 0
special_rate = 0

for i in range(1111, 10000):
    i_as_a_string = str(i)
    for j in range(0, len(i_as_a_string)):
        digit = int(i_as_a_string[j])

        if digit == 0:
            break
        else:
            if n % digit == 0:
                special_rate += 1


    if special_rate == 4:
        print(i, end=' ')
    special_rate = 0