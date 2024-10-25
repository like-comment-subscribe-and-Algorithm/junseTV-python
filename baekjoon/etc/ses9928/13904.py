# 하루 한 과제
# 마감일 존재
# 각각의 점수 존재
# 점수의 최댓값

import sys
import heapq

def solve(n, homeworks):
    assigned = dict()

    for i in range(1, n + 1):
        assigned[i] = 0
    homeworks.sort(key = lambda x: x[0])

    while homeworks:
        nowscore, nowdate = homeworks.pop()
        for i in range(n):
            if assigned[n - i] == 0 and n - i < nowdate + 1:
                assigned[n - i] = nowscore
                break
    answer = 0
    result = list(assigned.values())
    for i in result:
        answer += i
    return answer

input = sys.stdin.readline

n = int(input())
homeworks = []

for _ in range(n):
    d, w = list(map(int, input().split(' ')))
    heapq.heappush(homeworks, (w, d))

print(solve(n, homeworks))