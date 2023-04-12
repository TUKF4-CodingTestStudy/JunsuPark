import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
bridge = [[] for _ in range(N + 1)]


def BFS(c):
    queue = deque([factor1])
    visited = [False] * (N + 1)                     # 노드 방문했는지 확인
    visited[factor1] = True
    while queue:
        x = queue.popleft()
        for y, weight in bridge[x]:
            if not visited[y] and weight >= c:      # 방문하지 않았으면서 다리의 가중치가 트럭의 가중치보다 크다면(이동 가능)
                visited[y] = True                   # 방문했음을 표시
                queue.append(y)                     # 큐에 삽입
    return visited[factor2]                         # 탐색이 끝나고 마지막 공장까지 도달할 수 있다면 True , 없다면 False


start = 100000000
end = 1
for _ in range(M):
    x, y, weight = map(int, input().split())
    bridge[x].append((y, weight))
    bridge[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

factor1, factor2 = map(int, input().split())

result = start
while start <= end:
    mid = (start + end) // 2  # mid는 현재의 중량을 의미
    if BFS(mid):  # 이동이 가능하므로 중량을 증가시킨다.
        result = mid
        start = mid + 1
    else:  # 이동이 불가능하므로 중량을 감소시킨다.
        end = mid - 1

print(result)

# C의 범위는 1,000,000,000으로 굉장히 크므로 C에대가 이진탐색(log)을 적용한다고 생각하면 된다.
# https://www.acmicpc.net/problem/1939