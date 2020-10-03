def combinations(line, index):
    if index >= len(line):
        print(''.join(line))
        return
    combinations(line, index + 1)
    for i in range(index + 1, len(line)):
        line[index], line[i] = line[i], line[index]
        combinations(line, index + 1)
        line[index], line[i] = line[i], line[index]


text = list(input())
combinations(text, 0)


# def print_comb(text1, idx):
#     if idx >= len(text1):
#         print(''.join(text1))
#         return
#     print_comb(text1, idx + 1)
#     for i in range(idx + 1, len(text1)):
#         text1[idx], text1[i] = text1[i], text1[idx]
#         print_comb(text1, idx + 1)
#         text1[idx], text1[i] = text1[i], text1[idx]
#
#
# text1 = list(input())
# print_comb(text1, 0)

# def fibo(n):
#     if n == 0:d
#         return 0
#     if n == 1:
#         return 1
#
#     return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(7))


# def finder(n):          # Factoriel finding recursion
#     if n == 0:
#         return 1
#     return n * finder(n - 1)
