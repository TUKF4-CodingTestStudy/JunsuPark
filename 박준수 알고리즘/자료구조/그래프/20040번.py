import sys

input = sys.stdin.readline


def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 = find_parent(parent, node2)
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2


n, m = map(int, input().split())
parent = [i for i in range(n)]
cycle = False
count = 1

for i in range(m):
    node1, node2 = map(int, input().split())
    if find_parent(parent, node1) == find_parent(parent, node2):
        cycle = True
        break
    else:
        union_parent(parent, node1, node2)
        count += 1


if cycle:
    print(count)
else:
    print(0)

# 부모 노드를 만든다
# 부모 노드는 맨처음 자기 자신의 노드를 가르킨다.
# 두 노드의 부모 노드가 같다는 것은 --> cycle이 형성 되었다는 것!
# 두 부모 노드가 다르면 각 노드의 부모 노드를 찾고 부모노드가 더 큰 쪽을 -> 연결 노드로 바꾸어 서로 연결됬음을 표시
# union-find문제
# https://www.acmicpc.net/problem/20040