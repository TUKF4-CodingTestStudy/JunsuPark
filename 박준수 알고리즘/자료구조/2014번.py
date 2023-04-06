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

        if num % prime[j] == 0:  # 2X3은 되지만 3X2는 안되게 반복 제거// 입력받은 소수로 나누어 떨어지는 경우
            break                   # 이 경우 까지만 힙에 삽입
else:
    print(num)

# https://www.acmicpc.net/problem/2014
# 1. 입력받은 소수들을 우선순위 큐에 넣는다. (우선순위 큐는 오름차순 기준)
# 2. 우선순위 큐에서 수를 하나 빼 내고, 그 수와 처음에 입력받은 소수들과 각각 곱한 후 우선순위 큐에 넣는다.
# 3. 2번 과정을 N번 반복한 후, 우선순위 큐에서 마지막으로 빼낸 값이 정답으로 출력한다.