from collections import deque

num_of_stations = int(input())
starting_points = deque(list())

for i in range(num_of_stations):
    station = input().split()
    station = list(map(int, station))
    starting_points.append(station)

for i in range(len(starting_points)):
    tank = 0
    distance = 0
    counter = 0
    success_counter = 0
    for j in range(len(starting_points)):
        current = starting_points[counter]
        fuel = current[0]
        tank += fuel
        distance = current[1]
        if tank >= distance:
            success_counter += 1
            tank -= distance
        else:
            break
        counter += 1
    if success_counter == len(starting_points):
        print(i)
        break
    else:
        go_back = starting_points.popleft()
        starting_points.append(go_back)
