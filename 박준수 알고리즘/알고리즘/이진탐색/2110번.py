import sys
input = sys.stdin.readline

N, C = map(int, input().split())

x = []
for _ in range(N):
    x.append(int(input()))
x.sort()

start = 1 # 최소 gap
end = x[-1] - x[0] # 최대 gap
result = 0

while start <= end:
    mid = (start + end) // 2 # 중간 gap
    value = x[0]
    count = 1
    for i in range(1, len(x)):
        if x[i] >= value + mid:         # 앞 집부터 공유기를 설치, 현재 집에서 다음 집의 거리가 mid를 초과한다면 공유기를 설치 할 수 있음
            value = x[i]
            count += 1                  # 공유기 설치 수를 증가
    if count >= C:          # count가 C보다 크거나 같으면 gap차이를 너무 적게 두었기에 start를 mid + 1로 바꾸어 mid값(gap)을 늘린다.
        start = mid + 1
        result = mid
    else:                   # count가 C보다 작으면 gap 차이를 너무 크게 둔것이므로 end를 mid - 1로 바꾸어 mid값(gap)을 줄인다.
        end = mid - 1

print(result)

# 최솟값은 1, 최댓값은 집 사이가 가장 먼 gap, 중간값은 (최솟값+최댓값) // 2 중간gap
# https://www.acmicpc.net/problem/2110

#이진 탐색은 재귀적과 반복적으로 구현 가능