import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_dist, now = heapq.heappop(q)
        if distance[now] < now_dist:
            continue
        for new, new_dist in graph[now].items():
            cost = now_dist + new_dist
            if cost < distance[new]:
                distance[new] = cost
                heapq.heappush(q, (cost, new))
    return distance


def solution(n, s, a, b, fares):
    V = [i for i in range(1, n + 1)]
    graph = {v: {} for v in V}
    for edge in fares:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    dist = dijkstra(graph, s)
    result = []
    for v in V:
        dist2 = dijkstra(graph, v)
        result.append(dist[v] + dist2[a] + dist2[b])

    return min(result)