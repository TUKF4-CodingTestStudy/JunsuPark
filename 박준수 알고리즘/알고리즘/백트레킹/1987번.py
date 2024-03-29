# 이동 좌표 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global result

    # 동일한 경우는 한 번만 계산하기 위하여 집합(set) 자료형 사용
    q = set()
    q.add((x, y, board[x][y]))

    while q:
        x, y, step = q.pop()
        # 가장 긴 이동 거리를 저장
        result = max(result, len(step))

        # 네 방향 (상, 하, 좌, 우)으로 이동하는 경우를 각각 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 수 있는 위치이면서, 새로운 알파벳인 경우  ex) A가 CD에 포함안되어있어야 추가
            if (0 <= nx < r and 0 <= ny < c and
                    board[nx][ny] not in step):
                q.add((nx, ny, step + board[nx][ny]))


r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(input())

result = 0
bfs(0, 0)
print(result)
