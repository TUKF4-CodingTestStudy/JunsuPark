import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)

# 스택에는 원소의 인덱스를 넣어주는 목적
# 수열의 개수 동안 stack이 비어잇지 않거나 스택의 마지막 원소가 인덱스인 A원소가 i번째 수열의 원소보다 작을때동안 반복
# 스택의 마지막 원소를 인덱스로한 answer리스트에 A[i]값을 대입
# 스택이 비어있거나 스택의 마지막 원소를 인덱스로한 A원소가 A[i]보다 크거나 같으면 스택에다 i를 추가

# https://www.acmicpc.net/problem/17298