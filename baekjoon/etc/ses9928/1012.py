import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t = int(input())

answer = []

def dfs(start):
    global xs
    global visited
    global move

    x, y = start
    xs[y][x] = 2

    for i in move:
        nx, ny = x + i[0], y + i[1]
        if nx not in range(m):
            continue
        if ny not in range(n):
            continue
        if xs[ny][nx] == 1:
            dfs((nx, ny))

for each in range(t):
    m, n, k = list(map(int, input().split(' ')))

    xs = [[0 for _ in range(m)] for _ in range(n)]
    xs2 = list()

    for i in range(k):
        x, y = list(map(int, input().split(' ')))
        xs[y][x] = 1
        xs2.append((x, y))

    visited = []

    result = 0

    for i in xs2:
        x, y = i
        if xs[y][x] == 1:
            result += 1
            dfs((x, y))

    answer.append(result)

for i in answer:
    print(i)