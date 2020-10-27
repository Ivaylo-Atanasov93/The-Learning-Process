def palindrome(a):
    reversed_a = a[::-1]
    if a == reversed_a:
        print('True')
    else:
        print('False')


string = input().split(', ')

for i in string:
    palindrome(i)