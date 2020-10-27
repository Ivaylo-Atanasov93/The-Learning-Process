def solve(string):
    result = []
    for i in range(len(string)):
        result.append(int(string[-1]))
        string.pop()
    for num in result:
        print(num, end=' ')

solve(input().split())