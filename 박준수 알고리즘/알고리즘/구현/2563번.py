N = int(input())
array = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x1, y1 = map(int, input().split())

    for row in range(x1, x1 + 10):
        for col in range(y1, y1 + 10):
            array[row][col] = 1

result = 0

for i in array:
    result += i.count(1)

print(result)

# 100, 100좌표가 있는 테이블을 생성
# 정사각형 범위에 0->1 로 변경
# 1만 적혀 있는 갯수를 셈
# https://www.acmicpc.net/problem/2563