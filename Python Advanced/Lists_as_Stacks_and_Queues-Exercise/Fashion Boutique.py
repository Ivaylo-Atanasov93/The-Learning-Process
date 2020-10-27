clothes = input().split()
capacity = int(input())
clothes = list(map(int, clothes))
used_racks = 0

while clothes:
    counter = 0
    while counter < capacity:
        current = clothes.pop()
        counter += current
        if counter > capacity:
            used_racks += 1
            clothes.append(current)
        if counter == capacity and clothes:
            used_racks += 1
    if sum(clothes) <= capacity:
        used_racks += 1
        break

print(used_racks)