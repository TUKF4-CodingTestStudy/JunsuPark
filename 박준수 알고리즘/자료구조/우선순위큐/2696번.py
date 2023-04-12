import sys
input = sys.stdin.readline
import heapq

def show_result():
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
        if(i+1) % 10 == 0:
            print()
    print()

for _ in range(int(input())): # 테스트 케이스만큼 반복
    m = int(input()) # 수열의 크기 입력
    data = []
    for i in range(m // 10 + 1):
        data.extend(list(map(int, input().split())))
    left = [] #왼쪽 최대 힙(중앙값보다 작은 값을 넣는다)
    right = [] #오른쪽 최소 힙(중앙값보다 큰 값을 넣는다)
    median = data[0]
    result = [median]
    for i in range(1, m):
        if data[i] <= median: heapq.heappush(left, -data[i])
        else: heapq.heappush(right, data[i])
        if i % 2 == 0:      #   2개 확인할 때마다
            if len(left) > len(right):      # 왼쪽 힙과 오른쪽 힙을 맞춰준다.
                heapq.heappush(right, median)
                median = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -median)
                median = heapq.heappop(right)
            result.append(median)
    show_result()

# 최대 힙 - 중앙값 - 최소 힙 형태의 구조를 갖춘다.
# 새로운 원소가 들어왔을 때
#   - 중앙값보다 작거나 같은 원소는 왼쪽의 최대 힙에 넣는다.
#   - 중앙값보다 큰 원소는 오른쪽의 최소 힙에 넣는다.
# 홀수번째 원소가 입력될 때 마다 최대 힙과 최소 힙의 크기를 동일하게 맞춘다.
#   - 한쪽이 더 크다면, 반대쪽으로 이동시킨다.