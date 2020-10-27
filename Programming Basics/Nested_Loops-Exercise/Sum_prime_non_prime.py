# line = input()
#
# prime_sum = 0
# non_prime_sum = 0
# is_prime = True
#
# while line != 'stop':
#     line = int(line)
#     is_prime = True
#     if line < 0:
#         print('Number is negative.')
#         line = 0
#     else:
#         for i in range (2, line):
#             if line % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             prime_sum += line
#         else:
#             non_prime_sum += line
#
#     line = input()
#
# print(f'Sum of all prime numbers is: {prime_sum}')
# print(f'Sum of all non prime numbers is: {non_prime_sum}')

def is_prime(num):
    is_prime = True
    if num < 2:
        is_prime = False
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(f'{is_prime}, {num} is prime ')
    else:
        print(f'{is_prime}, {num} is not prime ')

is_prime(43)