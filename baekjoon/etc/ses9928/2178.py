import heapq

def di(graph, N, M):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distances = [[1e9 for _ in range(M)] for _ in range(N)]
    distances[0][0] = 1
    q = []
    heapq.heappush(q, (1, 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if cost > distances[y][x]:
            continue
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 0:
                continue
            ncost = cost + 1
            if ncost < distances[ny][nx]:
                distances[ny][nx] = ncost
                heapq.heappush(q, (ncost, nx, ny))

    return distances[N - 1][M - 1]

N, M = list(map(int, input().split()))
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
print(di(graph, N, M))