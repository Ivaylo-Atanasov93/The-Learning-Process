rooms = int(input())
chair_counter = 0
missing_chairs = 0
for i in range(rooms):
    chairs = input().split()
    if len(chairs[0]) >= int(chairs[1]):
        chair_counter += (len(chairs[0]) - int(chairs[1]))
    elif len(chairs[0]) < int(chairs[1]):
        print(f'{int(chairs[1]) - len(chairs[0])} more chairs needed in room {i + 1}')
        missing_chairs += (int(chairs[1]) - len(chairs[0]))

if chair_counter >= 0 and missing_chairs == 0:
    print(f'Game On, {chair_counter} free chairs left')
