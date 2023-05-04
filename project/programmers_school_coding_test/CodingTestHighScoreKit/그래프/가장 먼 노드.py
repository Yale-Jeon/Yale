from collections import defaultdict
import heapq


def solution(n, edge):
    graph = defaultdict(list)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    distance = [9999] * (n + 1)
    distance[0] = -1
    start = 1
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        now_dist, now = heapq.heappop(q)
        if distance[now] < now_dist:
            continue
        for v in graph[now]:
            if now_dist + 1 < distance[v]:
                distance[v] = now_dist + 1
                heapq.heappush(q, (now_dist + 1, v))

    x = max(distance)
    print(distance)
    print(x)
    return distance.count(x)