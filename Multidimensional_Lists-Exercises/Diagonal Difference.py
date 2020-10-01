num = int(input())
matrix = []
for _ in range(num):
    matrix.append([int(x) for x in input().split()])

p_d_sum = 0
s_d_sum = 0

for i in range(num):
    p_d_sum += matrix[i][i]

for i in range(1, num + 1):
    s_d_sum += matrix[i - 1][- i]

print(abs(p_d_sum - s_d_sum))