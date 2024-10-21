import sys
import heapq

input = sys.stdin.readline
n = int(input())
a, b = list(map(int, input().split()))

m = int(input())
graph = dict()

for i in range(n):
    graph[i + 1] = []

for i in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def di(graph, start, end):
    global n

    distances = [1e9 for _ in range(n + 1)]
    distances[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    visited = set()

    while q:
        cost, current = heapq.heappop(q)

        if distances[current] < cost:
            continue

        for ncurrent in graph[current]:
            if ncurrent in visited:
                continue
            visited.add(ncurrent)
            ncost = cost + 1
            if distances[ncurrent] > ncost:
                distances[ncurrent] = ncost
                heapq.heappush(q, (ncost, ncurrent))

    if distances[end] == 1e9:
        return -1
    else:
        return distances[end]

print(di(graph, a, b))