import sys

# 이진 트리를 돌면서 tree의 깊이를 매겨준다.
def dfs(cur, depth):
    global max_depth
    visited[cur] = True
    tree[cur][3] = depth
    if max_depth < depth:
        max_depth = depth

    for i in range(2):  # 왼쪽 자식 , 오른쪽 자식 순회
        if not visited[tree[cur][i]]:
            dfs(tree[cur][i], depth + 1)


# 중위순회를 돌면서 너비 번호를 매겨준다.
def in_order(v):
    global order

    if v:
        in_order(tree[v][0])
        tree[v][4] = order
        order += 1
        in_order(tree[v][1])


input = sys.stdin.readline
N = int(input())

tree = [[0, 0, 0, 0, 0] for i in range(N+1)] # 왼쪽 자식, 오른쪽 자식, 부모 ,깊이, 너비
for _ in range(N):
    node, left, right = map(int, input().split())

    if left == -1: left = 0
    if right == -1: right = 0

    tree[node][0] = left        # 자식 노드 선정
    tree[node][1] = right

    tree[left][2] = node        # 부모 노드 선정
    tree[right][2] = node

visited = [False] * (N+1)
visited[0] = True

# 루트 번호 찾기
root = 0
for i in range(1, N+1):
    if tree[i][2] == 0:
        root = i
        break

# 깊이의 최대치 찾기
max_depth = 0
dfs(root, 1)

order = 1 # 순서를 매길 번호
in_order(root)  # 중위 순회를 root번호부터 돈다.

# 각 깊이당 너비를 구하기 위해 최대깊이만큼 이중리스트 설정
depth_list = [[] for _ in range(max_depth + 1)]
for j in range(1, N+1):
    depth_list[tree[j][3]].append(tree[j][4])

result = []

for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1: # 만약 해당 깊이에 하나밖에 없다면 1을 넣어준다.
        result.append(1)
    else:   #  2개 이상이라면
        result.append(max(depth_list[i]) - min(depth_list[i]) + 1) # 가장 짧은 것과 긴것의 차 + 1을 넣어준다.

print(result.index(max(result), 1), max(result))

# DFS로 노드의 깊이를 매겨준다.
# 중위 순회로 노드의 너비 번호를 매겨준다.