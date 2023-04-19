import sys

input = sys.stdin.readline


def dfs(cur_node, depth):
    global max_depth
    visited[cur_node] = True
    tree[cur_node][3] = depth
    if max_depth < depth:
        max_depth = depth

    for i in range(2):      # 왼쪽 자식, 오른쪽 자식에 깊이를 넣는다.
        if not visited[tree[cur_node][i]]:
            dfs(tree[cur_node][i], depth + 1)


def in_order(cur_node):
    global order

    if cur_node:
        in_order(tree[cur_node][0]) # 왼쪽 노드
        tree[cur_node][4] = order   # root
        order += 1
        in_order(tree[cur_node][1]) # 오른쪽 노드

N = int(input())

tree = [[0, 0, 0, 0, 0] for i in range(N+1)] # 왼쪽 자식, 오른쪽 자식, 부모, 깊이, 너비 / 각 리스트는 노드의 데이터를 가지고 있음
for _ in range(N):
    node, left, right = map(int, input().split())

    if left == -1: left = 0
    if right == -1: right = 0

    tree[node][0] = left
    tree[node][1] = right

    tree[left][2] = node
    tree[right][2] = node

visited = [False] * (N+1)
visited[0] = True

# 루트 번호를 찾기
root = 0
for i in range(1, N+1):
    if tree[i][2] == 0:
        root = i
        break

# 깊이의 최대치 찾기
max_depth = 0
# dfs로 노드의 깊이를 매긴다.
dfs(root, 1)

# 순서를 매길 번호
order = 1
# 중위 순회로 root부터 돌아 너비를 매긴다.
in_order(root)


# 각 깊이당 너비를 구하기 위해 최대 깊이만큼 이중 리스트 설정
depth_list = [[] for _ in range(max_depth + 1)]
for j in range(1, N+1):
    depth_list[tree[j][3]].append(tree[j][4])


result = []

for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1:     # result의 인덱스 번호가 트리의 깊이가 된다.
        result.append(1)
    else:
        result.append(max(depth_list[i]) - min(depth_list[i]) + 1)

print(result.index(max(result), 1), max(result))