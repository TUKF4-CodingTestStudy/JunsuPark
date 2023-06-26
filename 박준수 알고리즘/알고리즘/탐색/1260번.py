from collections import deque


def dfs(V):  # dfs는 재귀 함수로 구현
    print(V, end=' ')
    visited[V] = True
    for e in adj[V]:
        if not (visited[e]):
            dfs(e)


def bfs(V):  # bfs는 덱으로 구현
    q = deque([V])
    while q:
        V = q.popleft()
        if not (visited[V]):
            visited[V] = True
            print(V, end=' ')
            for e in adj[V]:
                if not visited[e]:
                    q.append(e)


N, M, V = map(int, input().split())

adj = [[] for _ in range(N + 1)]  # 인접 리스트 생성

for _ in range(M):  # 각 정점의 간선 연결
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:  # 정점 번호가 작은것 부터 정렬
    e.sort()

visited = [False] * (N + 1)  # 방문 노드 확인 배열
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)
