from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([i+1 for i in range(N)])
result = []


while queue:
    count = 1
    while count != K:
        queue.append(queue.popleft())
        count += 1
    result.append(queue.popleft())

print('<', end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
print('>')

# https://www.acmicpc.net/problem/11866

# 원에서 K번째가 되면 popleft 안되면 popleft후 append로 오쪽 른향으로 원이 돌아간다.