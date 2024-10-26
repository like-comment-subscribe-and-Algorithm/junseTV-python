from itertools import combinations

aeiou = {'a', 'e', 'i', 'o', 'u'}

def solve(L, C, a, b):
    result = []
    for n in range(L - 3 + 1):
        if n + 1 > len(a):
            continue
        if 2 + L - 3 - n > len(b):
            continue
        newa = list(combinations(a, n + 1))
        newb = list(combinations(b, 2 + L - 3 - n))

        for i in newa:
            for j in newb:
                temp = []
                temp.extend(i)
                temp.extend(j)
                temp.sort()
                result.append(temp)
    return sorted(result)

L, C = list(map(int, input().split(' ')))
possible = list(map(str, input().split(' ')))
a = [] # 모음
b = [] # 자음
for i in possible:
    if i in aeiou:
        a.append(i)
    else:
        b.append(i)

answer = solve(L, C, a, b)
for i in answer:
    temp = ''
    print(temp.join(i))