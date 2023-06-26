from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX   # 각 위치(인덱스)가 이동 할 수 있는 위치값 배열


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:           # 같은 위치에 도달하게 되면
            return array[now_pos]  # 위치로 이동한 연산의 횟수를 반환
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos <= MAX and not array[next_pos]:  # 범위 내에 있고 방문하지 않았다면
                array[next_pos] = array[now_pos] + 1          # 각 위치에 지금껏 연산된 횟수를 저장
                q.append(next_pos)


print(bfs())


# 이동 시간이 모두 1초로 동일하므로 BFS를 이용해 해결할 수 있음


# def dfs(V):
#     time = 0
#     q = deque([V])
#     while q:
#         V = q.popleft()
#         if V == K: break
#         if not visited[V]:
#             visited[V] = True
#             time += 1
#             for e in adj[V]:
#                 if not visited[e]:
#                     q.append(e)
#     print(time)
#
#
# N, K = map(int, input().split())
#
# adj = [[] for _ in range(100001)]
#
# adj[0].append(0)
# for i in range(1, 100001):
#     if i * 2 <= 100000:
#         adj[i].append(i * 2)
#     if i + 1 <= 100000:
#         adj[i].append(i + 1)
#     if i - 1 <= 100000:
#         adj[i].append(i - 1)
#
# visited = [False] * 100001
# dfs(N)
