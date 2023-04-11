bird_num = int(input())

count = 1

time = 0
while bird_num > 0:
    if count > bird_num:
        count = 1
    bird_num -= count
    time += 1
    count += 1

print(time)
# https://www.acmicpc.net/problem/1568