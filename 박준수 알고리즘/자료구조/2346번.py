import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque(map(int, input().split(" ")))
queue = deque((i, idx + 1) for idx, i in enumerate(queue))
result = []

while queue:
    paper, idx = queue.popleft()
    result.append(idx)

    if paper > 0:
        queue.rotate(-(paper - 1))
    elif paper < 0:
        queue.rotate(-paper)

print(' '.join(map(str, result)))

# deque의 rotate는 음수를 넣게 된다면 왼쪽 회전, 양수는 오른쪽 회전
# 오른쪽 회전 : pop -> appendleft
# 왼쪽 회전 : popleft -> append
# https://www.acmicpc.net/problem/2346