from collections import deque

quanity = int(input())
que = input().split()
que = deque(list(map(int, que)))
done = False
print(max(que))

while not done:
    if que:
        current_order = que.popleft()
        if current_order <= quanity:
            quanity -= current_order
        else:
            que.appendleft(current_order)
            done = True
            break
    else:
        break

if not que:
    print('Orders complete')
else:
    print('Orders left: ', end='')
    [print(order, end=' ') for order in que]
