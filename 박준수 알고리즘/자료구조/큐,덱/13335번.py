import sys
from collections import deque
input = sys.stdin.readline
count = 0

truck_num, bridge_length, bridge_weight = list(map(int, input().split()))
truck_queue = deque(map(int, input().split()))
bridge_queue = [0]*bridge_length

# 반복문을 통해 다리의 모든 트럭이 지날때까지 반복
while bridge_queue:
    count += 1  # 카운트
    bridge_queue.pop(0) # 다리의 칸을 하나씩 주린다.

    # 모든 트럭을 확인
    if truck_queue:
        # 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가 다리의 하중보다 크다면 빈 공간을 추가
        if sum(bridge_queue) + truck_queue[0] > bridge_weight:
            bridge_queue.append(0)
        # 다리의 하중보다 작다면 트럭을 다리에 추가
        else:
            bridge_queue.append(truck_queue.popleft())

print(count)

# - 반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복한다.
#
# - 모든 트럭을 확인하고 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가 다리의 하중보다 크다면 빈 공간을 추가한다.
#
# - 반대로 다리의 하중보다 작다면 트럭을 다리에 추가한다.
#
# - 위 방법을 반복하면 모든 트럭이 다 지나가고 다리의 칸이 0이 되어 반복이 멈춘다.
#
# - 이때 카운트를 출력한다.

# https://www.acmicpc.net/problem/13335