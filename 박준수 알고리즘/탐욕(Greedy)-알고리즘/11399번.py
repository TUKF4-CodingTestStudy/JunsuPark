N = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0

for index in range(len(time)):
    result += sum(time[0:index + 1])

print(result)

# https://www.acmicpc.net/problem/11399