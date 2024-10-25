import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
test = dict()

for i in range(n):
    test[i] = []

for i in range(m):
    a, b, c = list(map(int, input().split(' ')))
    test[a - 1].append((c, b - 1))

def di(test, start):
    global n

    q = []
    heapq.heappush(q, (0, start))
    distances = [1e9 for _ in range(n)]
    distances[start] = 0

    while q:
        cost, pos = heapq.heappop(q)

        if cost > distances[pos]:
            continue

        for i in test[pos]:
            ncost, npos = i[0] + cost, i[1]

            if ncost < distances[npos]:
                distances[npos] = ncost
                heapq.heappush(q, (ncost, npos))

    for i in range(n):
        if distances[i] == 1e9:
            distances[i] = 0

    return distances

answer = []
for i in range(n):
    answer.append(di(test, i))

result = ''
for i in range(n):
    line = ''
    for j in range(n):
        line += str(answer[i][j])
        if j != n - 1:
            line += ' '
    result += line
    if i != n - 1:
        result += '\n'
print(result)