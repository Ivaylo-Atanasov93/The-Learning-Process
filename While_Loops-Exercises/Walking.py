steps = input()
sum_of_the_steps = 0


if steps != 'Going home':
    steps = int(steps)
    sum_of_the_steps = sum_of_the_steps + steps

    while sum_of_the_steps < 10000:
        steps = input()
        if steps == 'Going home':
            steps = int(input())
            sum_of_the_steps = sum_of_the_steps + steps
            break
        steps = int(steps)
        sum_of_the_steps = sum_of_the_steps + steps

else:
    steps = int(input())
    sum_of_the_steps = sum_of_the_steps + steps

if sum_of_the_steps >= 10000:
    print('Goal reached! Good job!')
else:
    print(f'{10000 - sum_of_the_steps} more steps to reach goal.')