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


N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    union_parent(parent, node1, node2)


counter = set()
for i in range(1, N+1):
    counter.add(find_parent(parent, i))

print(len(counter))

# union함수를 쓰면 해당 노드가 가르키는 완벽한 부모 노드를 저장하고 있지 않을 수 있음
# 각 부모 노드의 원소가 가르키는 부모 노드를 set에다 추가해 길이를 반환

# https://www.acmicpc.net/problem/11724