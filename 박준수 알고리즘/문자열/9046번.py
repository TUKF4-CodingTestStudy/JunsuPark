

T = int(input())


for _ in range(T):
    message = input().replace(' ', '')
    alpabet_arr = [0] * 26

    for j in message:
        alpabet_arr[ord(j) - 97] += 1
    if alpabet_arr.count(max(alpabet_arr)) > 1:
        print('?')
    else:
        print(chr(97 + alpabet_arr.index(max(alpabet_arr))))
