import heapq

move = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

answer = []

def findspot(building, L, R, C):
    start = (-1, -1, -1)
    end = (-1, -1, -1)

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    start = (k, j, i)
                elif building[i][j][k] == 'E':
                    end = (k, j, i)
                if start != (-1, -1, -1) and end != (-1, -1, -1):
                    return start, end

def solve(building, start, end, L, R, C):
    global move
    q = []
    heapq.heappush(q, (0, start))
    startx, starty, startz = start
    distances = [[[1e9 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    distances[startz][starty][startx] = 0

    while q:
        cost, pos = heapq.heappop(q)
        x, y, z = pos

        if cost > distances[z][y][x]:
            continue

        for i in move:
            nx, ny, nz = x + i[0], y + i[1], z + i[2]
            ncost = cost + 1

            if nx not in range(C) or ny not in range(R) or nz not in range(L):
                continue

            if building[nz][ny][nx] == '#':
                continue

            if ncost < distances[nz][ny][nx]:
                distances[nz][ny][nx] = ncost
                heapq.heappush(q, (ncost, (nx, ny, nz)))

    endx, endy, endz = end

    if distances[endz][endy][endx] == 1e9:
        return 'Trapped!'
    else:
        return f'Escaped in {distances[endz][endy][endx]} minute(s).'

while True:
    L, R, C = list(map(int, input().split(' ')))
    if L == 0 and R == 0 and C == 0:
        break
    building = []
    for i in range(L):
        stair = []
        for j in range(R + 1):
            line = list(input())
            if line != []:
                stair.append(line)
        building.append(stair)
    start, end = findspot(building, L, R, C)
    answer.append(solve(building, start, end, L, R, C))

for i in answer:
    print(i)