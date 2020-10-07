class ValueCannotBeNegative(Exception):
    pass

for i in range(5):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegative
    print(x)