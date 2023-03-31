#
# n = int(input())
#
# count = 1
# stack = []
# result = []
#
# for i in range(1, n + 1): # 데이터 개수만큼 반복
#     data = int(input())
#     while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
#         stack.append(count) # 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자
#         count += 1
#         result.append('+')
#
#     if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
#         stack.pop()         # pop 했을 때의 숫자 나열이 처음 입력했던 data 숫자 나열과 같아야 함
#         result.append('-')
#     else: # 불가능한 경우
#         print('\nNO')
#         exit(0)
#
# print('\n'.join(result)) # 가능한 경우

# https://www.acmicpc.net/problem/1874


n = int(input())
count = 1
stack = []
result = []
for _ in range(n):
    num = int(input())
    for i in range(count, num+1):
        stack.append(i)
        result.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("\nNO")
        exit(0)

print('\n'.join(result))