import heapq
import sys

input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:  # 삭제 연산
        if len(heap) == 0:  # heap이 비어있다면
            print(0)
        else:               # heap이 비어있지 않으면
            absolute, original = heapq.heappop(heap)
            print(original)
    else:   # 삽입 연산
        heapq.heappush(heap, (abs(x), x))       # 첫번쨰 원소를 기준으로 우선순위 큐가 생성이 됨

# https://www.acmicpc.net/problem/11286