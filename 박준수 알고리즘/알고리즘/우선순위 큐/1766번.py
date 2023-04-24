import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
array = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

heap = []


for _ in range(M):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1    #진입차수를 증가시킴

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')

# 위상 정렬 알고리즘
# 1) 진입 차수가 0인 정점을 큐에 삽입합니다.
# 2) 큐(힙)에서 원소를 꺼내 해당 원소와 간선을 제거합니다.
# 3) 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입합니다.
# 4) 큐가 빌 때까지 2)-3) 과정을 반복합니다.

# - 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것이다.
# - 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과이다.
# https://www.acmicpc.net/problem/1766