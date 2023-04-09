import sys

input = sys.stdin.readline

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]
array.sort(key=lambda point: (point[0], point[1]))


for i in range(N):
    print(*array[i])

# 파이썬의 기본 정렬 라이브러리는 기본적으로 튜플,리스트의 인덱스 순서대로 오름차순 정렬한다.
# 따라서 array.sort()만 으로도 답이 도출됨/ 다음은 람다식으로도 적을 수 있음
# https://www.acmicpc.net/problem/11650