from collections import deque

firstinput = list(map(int, input().split(' ')))
m = firstinput[0]
n = firstinput[1]
h = firstinput[2]

tomatobox = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

q = deque()

for i in range(h):
    for j in range(n):
        secondinput = list(map(int, input().split(' ')))
        for k in range(m):
            tomatobox[i][j][k] = (secondinput[k], 0)
            if secondinput[k] == 1:
                q.append((k, j, i))


move = {(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)}
date = 0

while q:
    x, y, z = q.popleft()

    for i in move:
        dx, dy, dz = i
        if x+dx >= m or y+dy >= n or z+dz >= h or x+dx < 0 or y+dy < 0 or z+dz < 0:
            continue
        moved = tomatobox[z+dz][y+dy][x+dx]
        if moved[0] == 0:
            newdate = tomatobox[z][y][x][1] + 1
            tomatobox[z+dz][y+dy][x+dx] = (1, newdate)
            if newdate > date:
                date = newdate
            q.append((x+dx, y+dy, z+dz))

for i in tomatobox:
    if date == -1:
        break
    for j in i:
        if date == -1:
            break
        for k in j:
            if k[0] == 0:
                date = -1
                break

print(date)