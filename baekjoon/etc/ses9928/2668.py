result = set()
visited = set()
visited2 = set()

def main():
    global result
    global visited
    n = int(input())
    graph = dict()
    for i in range(n):
        graph[i+1] = []
    for i in range(n):
        eachinput = int(input())
        graph[eachinput] = graph[eachinput] + [i+1]
    print(graph)
    for i in graph:
        for j in graph[i]:
            dfs(graph, j)
    print(len(result))
    for i in result:
        print(i)

def dfs(graph, start):
    global visited
    global result
    visited.add(start)
    for i in graph[start]:
        if i not in visited:
            visited[2]
        elif start == i:
            result.add(i)
            return

main()