# 데드라인 ,컵라면수 입력
# 데드라인 기준 오름차순 정렬
# 우선순위 큐에 컵라면 수를 넣음 (최소 힙)
# 데드라인에 맞게 우선순위의 개수를 맞춰 줌
# 마지막에 남은 컵라면의 수가 정답

import sys
import heapq
input = sys.stdin.readline

n = int(input())

homework = []
for _ in range(n):
    x, y = map(int, input().split())
    homework.append((y, x)) # (컵라면 수, 데드라인)

homework.sort(key=lambda x: x[1])

heap = []
for i in range(len(homework)):
    heapq.heappush(heap, homework[i])
    while homework[i][1] < len(heap):
        heapq.heappop(heap)

result = 0
for i in range(len(heap)):
    result += heap[i][0]
print(result)