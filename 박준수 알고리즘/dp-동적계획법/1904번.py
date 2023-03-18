n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for index in range(3, n + 1):
    dp[index] = (dp[index - 1] + dp[index - 2]) % 15746


print(dp[n])

#https://www.acmicpc.net/problem/1904