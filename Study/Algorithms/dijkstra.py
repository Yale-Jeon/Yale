import heapq
"""
dijkstra :

if vertex = '0', '1', '2', ...
graph = {'0': {'1': 5, '2': 3}, '1': {}, '2': { ... }
"""

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

"""
Prim: 

Edges = [[vertex1, vertex2, weight], ...]
"""

def Prim(Edges, start):
    Vertices = []
    for edge in Edges:
        if edge[0] not in Vertices:
            Vertices.append(edge[0])
        if edge[1] not in Vertices:
            Vertices.append(edge[1])
    graph = {}
    for Vertex in Vertices:
        graph[Vertex] = {}
    for v1, v2, weight in Edges:
        graph[v1][v2] = weight
        graph[v2][v1] = weight
    V = [start]
    E = []
    q = []
    cost = 0
    for i in graph[start]:
        heapq.heappush(q, (graph[start][i], i, start))

    while q:
        weight, vertex1, vertex2 = heapq.heappop(q)
        if vertex1 in V:
            continue
        V.append(vertex1)
        E.append([vertex2, vertex1, weight])
        cost += weight
        for v in V:
            for i in graph[v]:
                if i not in V:
                    heapq.heappush(q, (graph[v][i],i,v))
    return V, E, cost