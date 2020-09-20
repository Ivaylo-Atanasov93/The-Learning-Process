import sys
a = int(input())
b = int(input())
c = int(input())

def finding_smallest (a, b, c):
    array = [a, b, c]
    return min(array)

print(finding_smallest(a, b, c))