n = int(input())

for i in range(n):
    pwd = input()
    left_stack = []
    right_stack = []

    for char in pwd:
        if char == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)

    left_stack.extend(reversed(right_stack))  # 오른쪽 스택에 남아 있는 경우도 있으므로 반대로 해서 추가한다.
    print(''.join(left_stack))

# 핵심 아이디어
# 1. 스택 2개를 만들고, 스택 두개의 중간 지점을  커서로 간주한다.
# 2. 문자입력 : 왼쪽 스택에 원소를 삽입
# 3. - 입력: 왼쪽 스택에서 원소를 삭제
# 4. < 입력: 왼쪽 스택에서 오른쪽 스택으로 원소를 이동
# 5. > 입력 : 오른쪽 스택에서 왼쪽 스택으로 원소를 이동


# https://www.acmicpc.net/problem/5397