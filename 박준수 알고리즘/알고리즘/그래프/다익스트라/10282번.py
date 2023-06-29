import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))   # (가중치 , 시작노드) 가중치를 기준으로 최소 힙을 생성
    distance[start] = 0     # 첫 시작 노드는 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]  # 가중치 합 계산
            if distance[i[0]] > cost:  # 원래의 가중치보다 더 작으면
                distance[i[0]] = cost   # 갱신
                heapq.heappush(heap_data, (cost, i[0]))

test_cast = int(input())

for _ in range(test_cast):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]        # 그래프(인접 리스트) 초기화
    distance = [float('inf')] * (n + 1)     # 거리 테이블 초기화

    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s))               # 연결 노드와 간선(가중치) 연결
    distances = dijkstra(c)                 # 거리 태이블 반환


    count = 0                               # 감연된 컴퓨터 수 (정점 수)
    max_distance = 0                        # 노드 연결 거리

    for i in distance:
        if i != float('inf'):
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)

# 최단 경로를 구함 -> 다익스트라 알고리즘 사용 할 수 있음