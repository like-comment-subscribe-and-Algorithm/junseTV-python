from itertools import combinations

def sum(numbers, S):
    sum = 0
    if len(numbers) == 0:
        return False
    for i in numbers:
        sum += i
    if sum == S:
        return True
    else:
        return False

answer = 0

N, S = list(map(int, input().split(' ')))
test = list(map(int, input().split(' ')))

for i in range(N + 1):
    temp = list(combinations(test, i))
    for j in temp:
        if sum(j, S):
            answer += 1

print(answer)