import heapq

def dijkstra(n, roads, start):
    # 각 노드까지의 최단 거리를 저장할 리스트, 초기값은 무한대
    distances = [float('inf')] * n
    distances[start] = 0  # 시작 노드의 거리는 0

    q = [(0, start)]  # 우선순위 큐 (비용, 노드)

    while q:
        current_cost, current_pos = heapq.heappop(q)

        # 이미 처리된 노드는 건너뜀
        if distances[current_pos] < current_cost:
            continue

        # 현재 노드와 연결된 이웃 노드들에 대해 거리 갱신
        for neighbor_pos, travel_cost in roads[current_pos]:
            new_cost = current_cost + travel_cost
            if new_cost < distances[neighbor_pos]:
                distances[neighbor_pos] = new_cost
                heapq.heappush(q, (new_cost, neighbor_pos))

    return distances

n, m, x = list(map(int, input().split(' ')))

roads = [[] for _ in range(n)]
reverse_roads = [[] for _ in range(n)]

# 도로 입력
for _ in range(m):
    start, end, cost = list(map(int, input().split(' ')))
    roads[start - 1].append((end - 1, cost))  # 정방향 도로
    reverse_roads[end - 1].append((start - 1, cost))  # 역방향 도로

# 1. X에서 다른 노드로 가는 최단 경로
to_nodes_from_x = dijkstra(n, roads, x - 1)

# 2. 다른 노드에서 X로 가는 최단 경로 (도로를 역방향으로 사용)
from_nodes_to_x = dijkstra(n, reverse_roads, x - 1)

# 3. 각 노드에서 X까지의 왕복 시간이 가장 긴 경우 계산
answer = 0
for i in range(n):
    answer = max(answer, to_nodes_from_x[i] + from_nodes_to_x[i])

print(answer)
