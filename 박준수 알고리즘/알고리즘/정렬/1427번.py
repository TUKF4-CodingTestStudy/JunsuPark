import sys
input = sys.stdin.readline

nums = input()
result = []

for i in range(len(nums)):
    result.append(nums[i])

result.sort()

for i in range(len(result)-1, 0, -1):
    print(result[i], end='')

# https://www.acmicpc.net/problem/1427