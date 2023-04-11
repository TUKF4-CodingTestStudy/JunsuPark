import sys
input = sys.stdin.readline

doc = list(input())
word = list(input())

doc.pop()
word.pop()
count = 0
while len(doc) != 0:
    i = 0
    length = i+len(word)
    if doc[i:i+length] == word[:]:
        count += 1
        del doc[i:length]
    else: del doc[0]

print(count)

# https://www.acmicpc.net/problem/1543