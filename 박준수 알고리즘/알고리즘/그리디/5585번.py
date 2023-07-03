

pay = int(input())

money = 1000 - pay
count = 0
moneyarr = [500, 100, 50, 10, 5, 1]

i = 0
while money > 0:
    result = money // moneyarr[i]
    count += result
    money = money % moneyarr[i]
    i += 1

print(count)