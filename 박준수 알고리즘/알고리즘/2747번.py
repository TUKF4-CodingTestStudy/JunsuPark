
n = int(input())

a,b = 0, 1
while n > 0:
    a,b = b, a+b
    n -= 1

print(a)

# def fibonacci(N):
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#     else:
#         return fibonacci(N - 1) + fibonacci(N - 2)
#
#
# N = int(input())
# print(fibonacci(N))

# 재귀함수를 쓴 피보나치 수열은 함수 호출이 너무 중복되어 시간 초과가 뜬다.
# https://www.acmicpc.net/problem/2747