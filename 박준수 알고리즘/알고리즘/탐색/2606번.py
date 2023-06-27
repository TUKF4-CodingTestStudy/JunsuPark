from collections import deque

# 나의 풀
def bfs(v):
    global count
    q = deque([v])
    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            for e in adj[v]:
                if not visited[e] and e not in q:
                    q.append(e)
                    count += 1
    return count


com_num = int(input())
com_con = int(input())

adj = [[] for _ in range(101)]

for _ in range(com_con):
    x, y = map(int, input().split())
    adj[x].append(y)

count = 0
visited = [False] * 101
print(bfs(1))


# def dfs(v):
#     global count
#     count += 1
#     visited[v] = True
#     for next_pos in adj[v]:
#         if not visited[next_pos]:
#             dfs(next_pos)
#
#
# dfs(1)
# print(count - 1)
# 정점의 개수가 적기에 사실 dfs로 푸는 방식이 좋다