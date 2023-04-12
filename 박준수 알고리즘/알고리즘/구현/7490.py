import copy

def reculsive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    reculsive(array, n)
    array.pop()

    array.append('+')
    reculsive(array, n)
    array.pop()

    array.append('-')
    reculsive(array, n)
    array.pop()

test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    reculsive([], n-1)

    integers = [i for i in range(1, n + 1)] # 숫자들 리스트

    for operators in operators_list:    # 연산의 수만큼 반복
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:  # 공백을 제거해서 숫자를 이어붙이게 한다.
            print(string)
    print()


# 자연수 N의 범위(3<=N<=9)가 매우 한정적이므로 완전 탐색으로 문제 해결
# 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산
#resculsive 함수에서 가능한 모든 경우를 고려하여 연산자 리스트를 만든다.
# ' ', '+', '-' 로 만들수 있는 연산자의 개수는 숫자의 개수가 n일떄 3^n-1개를 만들 수 있다.
# eval함수는 문자열 수식을 그대로 실행하는 함수 반환도 식에 따라 타입이 달라진다.

# https://www.acmicpc.net/problem/7490