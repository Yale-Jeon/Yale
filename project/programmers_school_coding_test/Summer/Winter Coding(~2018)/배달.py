import heapq

def solution(N, road, K):
    answer = 0
    distance = [99999999 for i in range(N + 1)]
    graph = {}
    for i in range(N):
        graph[i + 1] = {}
    for v1, v2, w in road:
        if v2 in graph[v1]:
            graph[v1][v2] = min(graph[v1][v2], w)
        else:
            graph[v1][v2] = w
        if v1 in graph[v2]:
            graph[v2][v1] = min(graph[v2][v1], w)
        else:
            graph[v2][v1] = w

    q = [(0, 1)]  # (dist, now)
    distance[1] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if distance[now] < now_dist:
            continue

        for v in graph[now]:
            if distance[v] > now_dist + graph[now][v]:
                distance[v] = now_dist + graph[now][v]
                heapq.heappush(q, (now_dist + graph[now][v], v))

    for d in distance:
        if d <= K: answer += 1
    print(distance)

    return answer