import hashlib

S = input().encode('utf-8')

hash_fun = hashlib.sha256()
hash_fun.update(S)
print(hash_fun.hexdigest())

# https://www.acmicpc.net/problem/10930
