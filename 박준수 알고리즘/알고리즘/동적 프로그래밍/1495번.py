n, s, m = map(int, input().split())

array = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j] == 0:
            continue
        if j - array[i - 1] >= 0:
            dp[i][j - array[i - 1]] = 1
        if j + array[i - 1] <= m:
            dp[i][j + array[i - 1]] = 1

result = -1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)

# i는 행 (곡의 수만큼)
# j는 열 (최대 볼륨의 수만큼, m)
# dp에는 볼륨이 가능하다면 1, 불가능하다면 0
# 마지막 곡에서(n) 1인것이 최댓값
# https://www.acmicpc.net/problem/1495