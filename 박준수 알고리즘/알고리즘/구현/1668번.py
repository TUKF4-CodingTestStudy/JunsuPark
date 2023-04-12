trophy_num = int(input())

shelf = [int(input()) for _ in range(trophy_num)]

left_count = 1
max = shelf[0]
for i in range(1, len(shelf)):
    if shelf[i] > max:
        left_count += 1
        max = shelf[i]
print(left_count)

right_count = 1
max = shelf[-1]
for j in range(len(shelf) - 2, -1, -1):
    if shelf[j] > max:
        right_count += 1
        max = shelf[j]
print(right_count)

# https://www.acmicpc.net/problem/1668