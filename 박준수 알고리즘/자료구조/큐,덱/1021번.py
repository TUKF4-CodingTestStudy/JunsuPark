import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

d = deque([i for i in range(1, n + 1)])     # 1~n+1까지 n개 덱에 저장
targets = list(map(int, input().split()))   # 인덱스 저장
cnt = 0

for target in targets:
    index = d.index(target)
    if index <= len(d) // 2:        # 왼쪽으로 돌리는게 더 빠른 경우
        for i in range(index):
            d.append(d.popleft())
            cnt += 1
    else:                            # 오른쪽으로 돌리는게 더 빠른 경우
        for i in range(len(d) - index):
            d.appendleft(d.pop())
            cnt += 1
    d.popleft()

print(cnt)

# https://www.acmicpc.net/problem/1021