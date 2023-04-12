# https://www.acmicpc.net/problem/2920

numbers = list(map(int, input().split()))
asc = True
des = True
for index in range(len(numbers) - 1):
    if numbers[index + 1] == numbers[index] + 1:
        des = False
    elif numbers[index + 1] == numbers[index] - 1:
        asc = False
    else:
        des = False
        asc = False
        print("mixed")
        break

if asc:
    print("ascending")
elif des:
    print("descending")

