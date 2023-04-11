castle_row, castle_col = map(int, input().split())
status = []

for _ in range(castle_row):
    status.append(input())

row = [0] * castle_row
col = [0] * castle_col

for i in range(castle_row):
    for j in range(castle_col):
        if status[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(castle_row):
    if row[i] == 0: row_count += 1

col_count = 0
for i in range(castle_col):
    if col[i] == 0: col_count += 1


print(max(col_count, row_count))


#https://www.acmicpc.net/problem/1236