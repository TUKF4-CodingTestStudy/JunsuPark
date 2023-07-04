import sys

n = int(input())
crane = list(map(int, input().split()))

m = int(input())
box = list(map(int, input().split()))

# 모든 박스를 옮길 수 없는 경우
if max(crane) < max(box):
    print(-1)
    sys.exit()

# 각 크레인이 현재 옮겨야 하는 박스의 번호(0부터 시작)
positions = [0] * n
# 각 박스를 옮겼는지의 여부
checked = [False] * m

# 최적의 해를 구해야 하므로, 내림차순 정렬
crane.sort(reverse=True)
box.sort(reverse=True)

result = 0
count = 0

while True:
    if count == len(box): # 박스를 다 옮겼다면 종료
        break
    for i in range(n): # 모든 크레인에 대하여 각각 처리
        while positions[i] < len(box):
            # 아직 안 옮긴 박스 중에서 옮길 수 있는 박스를 만날 때까지 반복
            if not checked[positions[i]] and crane[i] >= box[positions[i]]: # 안옮겨졌고 크레인이 옮길 수 있는 무게의 박스이면
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    result += 1
print(result)

# 매 분마다, 모든 크레인에 대하여 옮길 수 있는 박스를 선택하여 옮기도록 합니다
# 박스를 무게 기준으로 내림차순 정렬한 뒤에 무거운 것 부터 옮기도록 하면 됨

import sys

read = sys.stdin.readline

N = int(read())
cranes = list(map(int, read().split()))

M = int(read())
boxs = list(map(int, read().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if boxs[0] > cranes[0]:
    print(-1)
    sys.exit()
else:
    time = 0

    while boxs:
        if not boxs:
            break

        for crane in cranes:
            for box in boxs:
                if crane >= box:
                    boxs.remove(box)
                    break

        time += 1

    print(time)