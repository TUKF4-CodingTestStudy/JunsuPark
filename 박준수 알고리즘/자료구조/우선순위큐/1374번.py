import heapq
import sys

input = sys.stdin.readline

N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]

lecture.sort(key=lambda x: x[1])  # 시작 시간으로 오름차순 정렬
count = 0
min_heap = []  # 강의의 종료 시간을 담을 heap

for time in lecture:
    while min_heap and min_heap[0] <= time[1]:  # 강의 중 종료시간이 가장 빠른 시간보다 시작 시간이 크면 (겹치지 않는다)
        heapq.heappop(min_heap)                  # 가장 빠른 종료시간을 pop
    heapq.heappush(min_heap, time[2])           # 겹치게 된다면 종료시간을 push    (종료시간 갱신)
    count = max(count, len(min_heap))           # 최소 힙의 길이와 지금껏 count의 최댓값이 강이실의 개수개 된다.

print(count)

# https://www.acmicpc.net/problem/1374