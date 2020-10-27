def solve(expression):
    sub = []
    stack = []
    for i in range(len(expression)):
        if expression[i] == '(':
            stack.append(i)
        elif expression[i] == ')':
            sub.append(expression[int(stack[-1]):i + 1])
            stack.pop()
    [print(sub_ex) for sub_ex in sub]

solve(input())