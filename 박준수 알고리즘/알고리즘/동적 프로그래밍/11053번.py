N = int(input())
array = list(map(int, input().split()))
dp = [1] * N


for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# O(n^2)으로 수행 가능
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[i] < array[j]
# https://www.acmicpc.net/problem/11053