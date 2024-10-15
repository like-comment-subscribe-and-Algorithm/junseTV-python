from itertools import combinations

buildingcount = int(input())
buildings_without_pos = list(map(int,input().split(' ')))
buildings = list()

for i in range(len(buildings_without_pos)):
    buildings.append((i, buildings_without_pos[i]))

buildings_without_pos.clear()

def isvalid(current, other):
    global buildings
    first = (0,0)
    second = (0,0)

    if current[0] > other[0]:
        first = other
        second = current
    else:
        first = current
        second = other

    for i in range(first[0] + 1, second[0]):
        currentheight = ((second[1] - first[1])/(second[0] - first[0])) * (i - first[0]) + first[1]
        if buildings[i][1] >= currentheight:
            return False
    return True


def count(current):
    global buildings
    count = 0

    for i in buildings:
        if i[0] == current[0]:
            continue

        if isvalid(current, i):
            count += 1

    return count

answer = 0

for i in buildings:
    answer = max(count(i), answer)

print(answer)