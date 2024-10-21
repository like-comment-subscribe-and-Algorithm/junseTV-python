n = int(input())
count = 0

def solve(stack, next, n):
    global count

    x, y = next

    if y == n - 1:
        count += 1
        return

    stack[y] = x
    tempstack = set()

    for j in range(y + 1):
        temp = stack[j]
        tempstack.add(temp)

        if temp + y + 1 - j < n:
            tempstack.add(temp + y + 1 - j)

        if temp - y - 1 + j >= 0:
            tempstack.add(temp - y - 1 + j)

    for i in range(n):
        if i not in tempstack:
            solve(stack, (i, y + 1), n)
    return

for i in range(n):
    solve([-1 for _ in range(n)], (i, 0), n)

print(count)