N = int(input())
A = set(map(int, input().split(" ")))

M = int(input())
B = list(map(int, input().split(" ")))

for item in B:
    if item in A:
        print("1")
    else:
        print("0")

# https://www.acmicpc.net/problem/1920