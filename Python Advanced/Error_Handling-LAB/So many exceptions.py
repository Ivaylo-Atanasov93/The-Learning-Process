numbers_list = [[int(num) for num in input().split(', ')]]                #THE ORIGINAL TASK SOLUTION
result = 1

for list in numbers_list:
    for i in list:
        number = i
        if number <= 5:
            result *= number
        elif number > 5 and number <= 10:
            result /= number

print(result)

# numbers_list = []                                                        THIRD SOLUTION
#
# while True:
#     line = input()
#     if line == '':
#         break
#     numbers_list.append(line)
#     print('Press ENTER if that`s the final line of the input')
#
# for i in range(len(numbers_list)):
#     numbers_list[i] = [int(x) for x in numbers_list[i].split(', ')]
#
# for list in numbers_list:
#     result = 1
#     for i in list:
#         number = i
#         if number <= 5:
#             result *= number
#         elif number > 5 and number <= 10:
#             result /= number
#     print(result)

# numbers_list = [[int(num) for num in input().split(', ')]]      FIRST SOLUTION
# numbers_list.append([int(num) for num in input().split(', ')])
# numbers_list.append([int(num) for num in input().split(', ')])
# result = 1
#
# for list in numbers_list:
#     result = 1
#     for i in list:
#         number = i
#         if number <= 5:
#             result *= number
#         elif number > 5 and number <= 10:
#             result /= number
#     print(int(result))


# numbers_list = input().split(", ")                               THE ORIGINAL CODE
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)
