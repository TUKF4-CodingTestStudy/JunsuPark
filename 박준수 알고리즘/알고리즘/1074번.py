
N, r, c = map(int, input().split())

ans = 0

while N != 0:
    N -= 1

    # 1사분면
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0
    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)
    # 3사분면
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)
    # 4사분면
    else:
        ans += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(ans)

# 분활 정복 방법
# - 1사분면/ 2사분면 / 3사분면 / 4사분면으로 범위를 각각 나누고
# - 2, 3, 4사분면안에 있으면 각각 행이나 열을 이동시켜 분활 시킨 부분을 1사분면으로 이동시킨다는 생각
# 그 1사분면에서 다시 분활하여 숫자를 찾는 형식이다.
# https://www.acmicpc.net/problem/1074



# N, r, c = map(int, input().split())
#
# def sol(N, r, c):
#     if N == 0:
#         return 0
#     return 2*(r%2)+(c%2) + 4 *sol(N-1, int(r/2), int(c/2))
#
# print(sol(N, r, c))

# //규칙//
# 제일 작은 2*2 박스
# 0  1
# 2  3
# 로부터 각각 ( 0 제외 )
# 좌표r,c가 2배가 됨에 따라
# 값이 4의 배수로 확장하는 것을 볼 수 있습니다.
# 4*sol( N-1, int(r/2), int(c/2) ) 는
# 이제 4의 배수하기 이전의 값이라고 볼 수 있죠..! ( 이전 값의 좌표가 r // 2, c // 2 )

# 2*(r%2)+(c%2) ==> 2x2사각형 안에서 z방향으로 움직이는 횟수


# N = 3, r = 6, c = 2
# 0 + 4 X sol (2,3,1)
#
# N = 2, r = 3, c = 1
# 3 + 4 X sol(1,1,0)
#
# N = 1, r = 1, c = 0
# 2 + 4 X sol(0,0,0)