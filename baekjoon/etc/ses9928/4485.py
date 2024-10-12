import heapq

move = {(0,1), (1,0), (-1,0), (0,-1)}

def dik(graph):
    global move
    size = len(graph)
    distances = [[1e9 for _ in range(size)] for _ in range(size)]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if distances[y][x] < cost:
            continue

        for i in move:
            nx, ny = x + i[0], y + i[1]
            if nx >= size or ny >= size or nx < 0 or ny < 0:
                continue
            newcost = cost + graph[ny][nx]
            if distances[ny][nx] > newcost:
                distances[ny][nx] = newcost
                heapq.heappush(q, (newcost, nx, ny))

    return distances[size-1][size-1]

answer = []

while True:
    size = int(input())
    if size == 0:
        break
    matrix = []
    for i in range(size):
        matrix.append(list(map(int, input().split(' '))))
    answer.append(dik(matrix))

for i in range(len(answer)):
    print(f'Problem {i+1}: {answer[i]}')