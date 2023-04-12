from itertools import combinations

N, M = list(map(int, input().split()))
numbers = list(map(int, input().split()))

combi_num = [sum(combi) for combi in combinations(numbers, 3) if sum(combi) <= M]
print(max(combi_num))

# 카드 숫자에서 3개를 뽑고 3개 중 해당 숫자에 가장 가까운 숫자들의 합을 반환
# https://www.acmicpc.net/problem/2798