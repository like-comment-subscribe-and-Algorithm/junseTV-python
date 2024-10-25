import sys

sys.setrecursionlimit(10**8)

N = int(input())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(matrix, visited, start, n):
    global move
    visited.add(start)

    for i in move:
        nx, ny = start[0] + i[0], start[1] + i[1]
        if nx not in range(n) or ny not in range(n):
            continue
        if matrix[ny][nx] and (nx, ny) not in visited:
            dfs(matrix, visited, (nx, ny), n)

def solve(matrix, rain, n):
    safe = []
    new = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[j][i] > rain:
                new[j][i] = True
                safe.append((j, i))

    count = 0
    visited = set()

    for i in range(n):
        for j in range(n):
            if new[j][i] and (i, j) not in visited:
                dfs(new, visited, (i, j), n)
                count += 1

    return count

matrix = []
currentmax = 0

for _ in range(N):
    line = list(map(int, input().split(' ')))
    matrix.append(line)
    currentmax = max(max(line), currentmax)

answer = 1

for i in range(currentmax + 1):
    answer = max(solve(matrix, i, N), answer)

print(answer)