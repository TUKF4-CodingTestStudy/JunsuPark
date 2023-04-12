import sys

input = sys.stdin.readline

s1, s2, s3 = map(int, input().split())
count = [0]*81
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            count[i+j+k] += 1

print(count.index(max(count)))

# https://www.acmicpc.net/problem/1233