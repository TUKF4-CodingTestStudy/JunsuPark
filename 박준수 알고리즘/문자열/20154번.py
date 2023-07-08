alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='32123333113133122212112221'

count = 0
word = input()

for i in range(len(word)):
    count += int(numbers[alpha.index(word[i])])
    count %= 10

if count % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")