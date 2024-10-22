import heapq
import sys

input = sys.stdin.readline
m, n = list(map(int, input().split(' ')))

maze = []

for _ in range(n):
    temp = list(input())
    temp2 = []
    for i in range(m):
        temp2.append(int(temp[i]))
    maze.append(temp2)

def di():
    global n, m, maze

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distances = [[1e9 for _ in range(m)] for _ in range(n)]
    distances[0][0] = 0

    q = []
    heapq.heappush(q, (0, 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if distances[y][x] < cost:
            continue

        for i in move:
            nx, ny = x + i[0], y + i[1]

            if nx not in range(m) or ny not in range(n):
                continue

            ncost = cost + maze[ny][nx]

            if distances[ny][nx] > ncost:
                heapq.heappush(q, (ncost, nx, ny))
                distances[ny][nx] = ncost

    return distances[n - 1][m - 1]

print(di())