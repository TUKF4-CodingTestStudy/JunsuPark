import sys


def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


input = sys.stdin.readline  # 빠른 입력 함수
N = int(input())

stack = []

for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == "push":
        push(cmd[1])
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    elif cmd[0] == "top":
        top()

# https://www.acmicpc.net/problem/10828
