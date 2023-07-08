N = int(input())
num = int(input())
num_array = list(str(num))

sum = 0
for i in range(len(num_array)):
    sum += int(num_array[i])

print(sum)