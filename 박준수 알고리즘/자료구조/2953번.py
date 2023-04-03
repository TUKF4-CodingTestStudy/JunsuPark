import sys

input = sys.stdin.readline

scores = list(map(int, input().split(" ")))
idx = 0
max = sum(scores)
for i in range(1, 5):
    scores = list(map(int, input().split(" ")))
    if max < sum(scores):
        max = sum(scores)
        idx = i

print(idx+1, max)

# https://www.acmicpc.net/problem/2953
