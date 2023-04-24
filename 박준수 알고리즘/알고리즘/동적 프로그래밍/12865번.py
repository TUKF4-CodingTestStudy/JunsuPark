import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split())
dp =[[0] * (K+1) for i in range(N+1)] # K+1의 열, N+1행 으로 테이블을 만든다.

for i in range(1, N+1):  # i는 행
    weight, value = map(int, input().split())
    for j in range(1, K+1): # j는 열
        if j < weight:
            dp[i][j] = dp[i-1][j]   # weight 보다 작은 무게들은 그전 값으로 그대로 내려옴
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)   # weight보다 크거나 같은 무게들은 그전 값과 그전 값[j-weigt]열에 새로운 가중치를 더한 값 중 최댓값으로 갱시

print(dp[N][K])






# 모든 무게에 대하여 최대 가치를 저장하기
# D[i][j] = 배낭에 넣은 물품의 무게 합이 j 일때 얻을 수 있는 최대 가치
# 각 물품의 번호 i에 따라서 최대 가치 테이블 D[i][j]를 갱신하여 문제를 해결할 수 있다.
# https://www.acmicpc.net/problem/12865