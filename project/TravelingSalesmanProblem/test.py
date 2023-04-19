import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_dist, now = heapq.heappop()
        if distance[now] < now_dist:
            continue
        for new, new_dist in graph[now].items():
            cost = now_dist + new_dist
            if cost < distance[new]:
                distance[new] = cost
                heapq.heappush(q, (cost, new))