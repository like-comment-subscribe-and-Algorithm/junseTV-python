from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))

allP = []

for i in range(P[0]):
    allP.append('+')
for i in range(P[1]):
    allP.append('-')
for i in range(P[2]):
    allP.append('*')
for i in range(P[3]):
    allP.append('//')

permutation = set(permutations(allP, N - 1))

answer = -1000000000
answer2 = 1000000000

for i in permutation:
    line = A[0]
    for j in range(N - 1):
        if i[j] == '//' and line < 0:
            temp = line * (-1)
            line = int(eval(f'{temp}//{A[j + 1]}')) * (-1)
        else:
            line = int(eval(f'{line}{i[j]}{A[j + 1]}'))
    answer = max(answer, line)
    answer2 = min(answer2, line)

print(answer)
print(answer2)