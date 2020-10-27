# Solution No1
print('Solution No1')
text = input()

while True:
    try:
        num = int(input())
        break
    except ValueError:
        print('Variable times must be an integer')

print(text * num)


# Solution No2
print('Solution No2')
try:
    text = input()
    num = int(input())
    print(text * num)

except ValueError:
    print('Variable times must be an integer')

# Solution No3

def read_input():
    text = input()
    num = input()
    return text, num


def solve():
    result = ''
    text, num = read_input()
    try:
        result += text * int(num)
    except ValueError:
        result = 'Variable times must be an integer'
    return result

print('Solution No3')
print(solve())