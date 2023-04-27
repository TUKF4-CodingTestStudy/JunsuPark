first_string = list(input())
second_string = list(input())
dp = [[0] * (len(second_string)+1) for _ in range(len(first_string)+1)]

for i in range(1, len(first_string)+1):
    for j in range(1, len(second_string)+1):
        if first_string[i-1] == second_string[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(first_string)][len(second_string)])

# D[i][j]는 X[0...1]와 Y[0..1]의 공통 부분 수열의 최대 길이
# 두 문자열의 길이를 조금씩 늘려 가며 확인하여, 공통 부분 수열의 최대 길이를 계산함
# 문자열+1만큼 테이블 초기화
# 문자열이 같을 때 -> 왠쪽위 대각선 +1   // 현재 위치 기준
# 문자열이 다를 때 -> max(왼쪽, 위)    // 현재 위치 기준
# https://www.acmicpc.net/problem/9251