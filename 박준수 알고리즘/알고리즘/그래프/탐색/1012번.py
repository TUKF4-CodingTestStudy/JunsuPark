import sys
sys.setrecursionlimit(100000) # 재귀 함수가 너무 많아지면 처리시간 많이 걸리기 때문에 재귀 함수 호출 횟수 제한, 보통 10만번까지로 설정해줌


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)

# 연결 요소의 개수를 세는 문제