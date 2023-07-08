

while True:
    message = input()
    if message == "END":
        break
    print(message[::-1])

# lice에서 각각의 항목은 [start:stop:step]를 의미합니다.
# string[::-1]처럼 반대 방향으로 리스트의 데이터를 자를 수 있습니다.