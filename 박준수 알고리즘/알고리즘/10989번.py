import sys

input = sys.stdin.readline

N = int(input())

nums = [0] * 10001

for _ in range(N):
    num = int(input())
    nums[num] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)

# 계수 정렬(Counting Sort) 알고리즘
# 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법이다.
# 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정한다.
# 데이터가 등장한 횟수를 count하고
# 배열의 차례대로 갯수만큼 출력한다.
#https://www.acmicpc.net/problem/10989
