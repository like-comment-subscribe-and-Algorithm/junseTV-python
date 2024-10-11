from collections import deque

def bfs(start, end, convs):
    q = deque()
    q.append((start[0], start[1]))
    visited = []
    while q:
        x, y = q.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return 'happy'
        for i in convs:
            convsx, convsy = i
            if (convsx, convsy) not in visited:
                if abs(x - convsx) + abs(y - convsy) <= 1000:
                    visited.append((convsx, convsy))
                    q.append((convsx, convsy))

    return 'sad'

move = {(1,0), (-1,0), (0,1), (0,-1)}
n = int(input())
answer = []

for i in range(n):
    cons = int(input())
    home = list(map(int,input().split(' ')))
    start = (home[0], home[1])
    convs = []
    for i in range(cons):
        temp = list(map(int,input().split(' ')))
        convs.append((temp[0], temp[1]))
    festival = list(map(int, input().split(' ')))
    end = (festival[0], festival[1])
    answer.append(bfs(start, end, convs))

for i in answer:
    print(i)