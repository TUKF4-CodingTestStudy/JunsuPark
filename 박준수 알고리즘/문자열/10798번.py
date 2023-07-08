
words = [input() for i in range(5)]
for j in range(15):     # 각 단어의 자리수
    for i in range(5):  # 단어들의 개수
        if j < len(words[i]):
            print(words[i][j], end='')