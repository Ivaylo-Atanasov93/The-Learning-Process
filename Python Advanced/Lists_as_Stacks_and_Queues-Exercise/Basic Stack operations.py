def solve(first, second):
    quantity = int(first[0])
    for_pop = int(first[1])
    search = int(first[2])
    stack = [int(number) for number in second]
    for i in range(for_pop):
        stack.pop()
    if search in stack:
        print(True)
    else:
        print(min(stack))

solve(input().split(), input().split())