import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = list(map(int, input().split(' ')))

graph = dict()

def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        for i in graph[start]:
            dfs(graph, i, visited)

for i in range(n):
    graph[i] = []

for _ in range(m):
    start, end = list(map(int, input().split(' ')))
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)

count = 0
visited = set()

for i in range(n):
    if i not in visited:
        dfs(graph, i, visited)
        count += 1

print(count)
