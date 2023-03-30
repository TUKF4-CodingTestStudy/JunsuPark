def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


T = int(input())

for _ in range(T):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1


        union(x,y)
        print(number[find(x)])


# Union-Find 알고리즘 이용
# dictionary 자료형을 해쉬 처럼 이용

# 노드가 없으면 부모노드 만들고 숫자를 1로 초기화
# 처음에 노드가 dictionary에 없으면 노드와 네트워크 수 생성
# find함수는 노드와 부모 노드가 같으면 노드 리턴, 다르면 부모 노드 찾아서(재귀함수) (root)부모노드로 바꾸고 리턴
# union함수는 x,y의 부모 노드를 find함수로 찾고 서로 다르면 같은 노드로 부모 노드를 맞춰주고 바꾼 노드의 네트워크 수를 안바꾼 노드에 더해준다.
# x의 부모 노드를 찾아 네트워크 수를 출력


#부모 노드를 맞추어서 친구 네트워크를 연결하는 방식이다.
