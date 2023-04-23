import sys
import heapq

input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    add = first + second
    result += add
    heapq.heappush(heap, add)

print(result)

# https://www.acmicpc.net/problem/1715