
# 이분탐색 방법
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()			# A 정렬

for item in B:

    first, last = 0, N-1
    isExist = False

    while first <= last:
        medium = (first + last) // 2

        if item == A[medium]:
            print(1)
            isExist = True
            break
        elif item > A[medium]:
            first = medium + 1
        else:
            last = medium - 1

    if not isExist:
        print(0)


# 재귀 함수를 이용한 이진 탐색
# def binary_search(data, search):
#     if len(data) == 0:   # 이진 탐색에서 찾는 값이 없으면 0 리턴
#         return 0
#     elif len(data) == 1:
#         if data[0] == search:
#             return 1
#         else:
#             return 0
#
#     medium = len(data) // 2
#     if search == data[medium]:
#         return 1
#     else:
#         if search > data[medium]:
#             return binary_search(data[medium + 1:], search)
#         else:
#             return binary_search(data[:medium], search)
#
#
# N = int(input())
# A = list(map(int, input().split()))
#
# M = int(input())
# B = list(map(int, input().split()))
#
# A.sort()
#
# for item in B:
#     print(binary_search(A, item))



# 파이썬 문법을 사용한 방식
# N = int(input())
# A = set(map(int, input().split()))  시간을 줄이기 위해 중복 값이 없고 순서가 없는 set으로 한다.
#
# M = int(input())
# B = list(map(int, input().split()))
#
# for item in B:
#     print(1) if item in A else print(0)
