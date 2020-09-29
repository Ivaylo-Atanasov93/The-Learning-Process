from collections import deque


def hot_potato(people, number):
    people = deque(people)
    counter = 0
    while people:
        person = people.popleft()
        counter += 1
        if counter == number:
            counter = 0
            if people:
                print(f'Removed {person}')
            else:
                print(f'Last is {person}')
        else:
            people.append(person)


hot_potato(input().split(), int(input()))

# from collections import deque
#
#
# def hot_potato(people, number):
#     counter = 0
#     people = deque(people)
#     while len(people) > 1:
#         person = people.popleft()
#         counter += 1
#         if counter == number:
#             counter = 0
#             if len(people) == 1:
#                 print(f'Last is {person}')
#             else:
#                 print(f'Removed {person}')
#         else:
#             people.append(person)
#
# hot_potato(input().split(), int(input()))
