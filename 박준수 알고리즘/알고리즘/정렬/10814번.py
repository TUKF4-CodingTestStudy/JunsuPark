import sys

input = sys.stdin.readline

N = int(input())
users = []
for i in range(N):
    age, name = input().split()
    users.append([int(age), name])

users.sort(key=lambda x: x[0])

for i in range(len(users)):
    print(*users[i])

#https://www.acmicpc.net/problem/10814