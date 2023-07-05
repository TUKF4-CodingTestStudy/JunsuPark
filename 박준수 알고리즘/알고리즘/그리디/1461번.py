import heapq
import sys

input = sys.stdin.readline

plus_heap = []
minus_heap = []

n, m = map(int, input().split())
distances = list(map(int, input().split()))
distances.sort()

# 책의 개수가 1이면 무조건 거리는 1
if n == 1:
    print(1)
    sys.exit()

# 가장 거리가 먼 책까지의 거리
max_distance = max(max(distances), -min(distances))

for i in range(len(distances)):
    if distances[i] < 0:    # 책의 위치가 음수인 경우
        heapq.heappush(minus_heap, distances[i])
    else:                   # 책의 위치가 양수인 경우
        heapq.heappush(plus_heap, -distances[i])

distance_sum = 0

while len(minus_heap):
    distance_sum += -minus_heap[0]
    for i in range(m):
        heapq.heappop(minus_heap)
        if len(minus_heap) == 0:
            break

while len(plus_heap):
    distance_sum += -plus_heap[0]
    for i in range(m):
        heapq.heappop(plus_heap)
        if len(plus_heap) == 0:
            break

print(distance_sum * 2 - max_distance)

# 0 보다 큰 책들과 0보다 작은 책들을 나누어서 처리함
# 두 개의 우선순위 큐를 이용하여 문제를 해결할 수 있음
# 마지막 책을 놓을 때는 다시 0 으로 돌아올 필요가 없으므로, 가장 먼 책을 마지막으로 놓음
# 음수와 양수에 대하여 개별적으로 , M개씩 묶어서 처리함
# 왕복 거리(최솟값) : ( 각 거리의 합 ) * 2 - 가장 먼 책의 편도 거리
