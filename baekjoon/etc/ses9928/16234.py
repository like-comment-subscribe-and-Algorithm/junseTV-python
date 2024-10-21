from collections import deque

move = [(0,1), (0,-1), (1,0), (-1,0)]

def solution(graph, L, R, N):
    q = deque()
    temp = 0
    reset = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp += 1
            reset[j][i] = temp
    group = reset.copy()

    for i in range(N):
        for j in range(N):
            q.append((i, j))

    num = 0
    date = 0
    q2 = deque()

    while q2 or q:
        x, y = q.popleft()

        for i in move:
            dx, dy = i
            nx, ny = x + dx, y + dy

            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue

            if group[y][x] != group[ny][nx]:
                sub = abs(graph[y][x] - graph[ny][nx])
                if sub >= L and sub <= R:
                    num += 1
                    current = group[ny][nx]
                    past = group[y][x]
                    for j in range(N):
                        for k in range(N):
                            if group[k][j] == current:
                                group[k][j] = num
                            if group[k][j] == past:
                                group[k][j] = num
                    q2.append((nx, ny))

        if len(q) == 0:
            for i in q2:
                q.append(i)
            date += 1

    return date

N, L, R = list(map(int, input().split(' ')))

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split(' '))))

print(solution(matrix, L, R, N))