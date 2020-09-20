def perfect_number(number):
    proper_divisor_sum = 0
    for i in range(1, number):

        if number % i == 0:
            proper_divisor_sum += i

    if proper_divisor_sum == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)