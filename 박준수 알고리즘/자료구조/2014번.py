import sys
import heapq

input = sys.stdin.readline

K, N = list(map(int, input().split()))
prime = list(map(int, input().split()))

result = []
for num in prime:
    heapq.heappush(result, num)

for i in range(N):
    num = heapq.heappop(result)
    for j in range(K):
        new_num = num * prime[j]    # 뺀 값에 소수를 곱해서 새로운 값을 만든다.
        heapq.heappush(result, new_num)

        if num % prime[j] == 0:  # 2X3은 되지만 3X2는 안되게 반복 제거
            break
else:
    print(num)

# https://www.acmicpc.net/problem/2014