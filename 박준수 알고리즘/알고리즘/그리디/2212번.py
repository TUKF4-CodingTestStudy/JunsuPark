# 각 센서를 오름차순 정렬
# 각 센서 사이의 거리를 계산
# 가장 거리가 먼 순서대로 k-1개의 연결 고리를 제거
import sys

n = int(input())
k = int(input())

# 집중국의 개수가 센서의 개수보다 많으면 0 -> 종료
if k >= n:
    print(0)
    sys.exit()

censor = list(map(int, input().split()))
censor.sort()

distance = []
for i in range(len(censor)-1):
    distance.append(censor[i+1] - censor[i])

distance.sort()
for _ in range(k-1):
    distance.remove(max(distance)) # 가장 큰 거리부터 제거
print(sum(distance))