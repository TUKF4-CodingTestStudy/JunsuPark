import sys

input = sys.stdin.readline

alpa = [[chr(i), -1] for i in range(ord('a'), ord('z') + 1)]
check = [False] * len(alpa)

word = input().rstrip()

for i in range(len(word)):
    for j in range(len(alpa)):
        if word[i] == alpa[j][0] and check[j] == False:
            alpa[j][1] = i
            check[j] = True

for i in range(len(alpa)):
    print(alpa[i][1], end=" ")

# https://www.acmicpc.net/problem/10809