count = int(input())
brick = []
brick.append((0, 0, 0, 0))
for i in range(1, count + 1):
    size, height, weight = map(int, input().split())
    brick.append((i, size, height, weight))

# size에 따라 정렬
brick.sort(key=lambda x: x[3])

dp = [0] * (count+1)

for i in range(1, count + 1):
    for j in range(0, i):
        if brick[i][1] > brick[j][1]:
            dp[i] = max(dp[i], dp[j] + brick[i][2])

max_value = max(dp)
index = count
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(brick[index][0])
        max_value -= brick[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]

# i는 쌓인 벽돌의 번호를 행으로
# dp 테이블에는 벽돌의 번호마다 벽돌의 높이를 갱신
# max_value 위치부터 테이블을 역추적