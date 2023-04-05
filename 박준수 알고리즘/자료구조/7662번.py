# import heapq
# import sys
#
# input = sys.stdin.readline
#
#
# T = int(input())
#
# for _ in range(T):
#     heap = []
#     K = int(input())
#     for _ in range(K):
#         cmd = list(map(str, input().split()))
#         if cmd[0] == 'I':       # 삽입 연산
#             heapq.heappush(heap, int(cmd[1]))
#         if len(heap) != 0:      # 삭제 연산
#             if cmd[0] == 'D' and cmd[1] == '-1':
#                 heapq.heappop(heap)
#             elif cmd[0] == 'D' and cmd[1] == '1':
#                 heap.pop(heap.index(max(heap)))
#                 heapq.heapify(heap)
#         else:               # 우선순위 큐가 비어있다면
#             continue
#     if len(heap) == 0:
#         print("EMPTY")
#     else:
#         print(max(heap), min(heap))

import sys
import heapq

input = sys.stdin.readline


def pop(heap):
    while len(heap) > 0:
        data, id = heapq.heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None


for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []
    current = 0
    deleted = [False] * (k + 1)
    for i in range(k):
        command = input().split()
        operator, data = command[0], int(command[1])
        if operator == 'D':
            if data == -1:
                pop(min_heap)
            elif data == 1:
                pop(max_heap)
        elif operator == 'I':
            heapq.heappush(min_heap, (data, current))
            heapq.heappush(max_heap, (-data, current))
            current += 1

    max_value = pop(max_heap)  # 최댓값을 찾기위해 pop
    if max_value is None:
        print("EMPTY")
    else:
        # max_value는 deleted로 싱크를 맞춰줘서 min_heap에서도 꺼내지므로 다시 넣어야함
        heapq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))

# https://www.acmicpc.net/problem/7662