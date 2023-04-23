import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0 and len(heap) != 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

# https://www.acmicpc.net/problem/1927