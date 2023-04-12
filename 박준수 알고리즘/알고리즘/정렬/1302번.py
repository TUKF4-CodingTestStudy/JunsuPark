book_num = int(input())

count = 1
book_list = dict()
for _ in range(book_num):
    book_name = input()
    if book_name in book_list:
        book_list[book_name] += 1
    else:
        book_list[book_name] = count
sorted_book_list = sorted(book_list.items(), key=lambda x: (-x[1], x[0]))
# 값을 기준으로 내림차순 정렬 후 키를 기준으로 오름차순 정렬한다.

print(sorted_book_list[0][0])

# https://www.acmicpc.net/problem/1302