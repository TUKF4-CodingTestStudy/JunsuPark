# x번째 행에 놓은 Queen에 대하여 검증
def check(x):
    # 이전 행에 놓았던 모든 퀸들을 확인
    for i in range(x):
        if row[x] == row[i]:    # 위쪽 확인
            return False
        if abs(row[x] - row[i]) == x - i:   # 대각선 확인 / 열 - 열 = 행 - 행이 같으면 두개는 같은 대각 ㄷ
            return False
    return True



# x번째 행에 대하여 처리
def dfs(x):
    global result
    if x == n:  # 각 행이 전부 돌았을 때
        result += 1
    else:
        # x번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i  # x번째 행에 i열에 퀸을 둔다고 가정
            if check(x):    # 해당위치에 Queen을 두어도 괜찮은 경우
                dfs(x+1)    # 다음 행으로 이동




n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)