n = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])

# 빈리스트 만들기
# 입력값에 따른 배열 초기화
# 점화식 구하기
# 특정 입력값 리스트에서 추출

# acmicpc.net/problem/1904