sequence = input()
open_brackets = ['(', '{', '[']
closing_brackets = [')', '}', ']']
def balanced(sequence):
    stack = []
    for bracket in sequence:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            index = closing_brackets.index(bracket)
            if len(sequence) > 0 and open_brackets[index] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

print(balanced(sequence))

# def check(my_string):
#     brackets = ['()', '{}', '[]']
#     while any(x in my_string for x in brackets):
#         for br in brackets:
#             my_string = my_string.replace(br, '')
#     return not my_string
#
#
# string = input()
# print("YES"
#       if check(string) else "NO")
