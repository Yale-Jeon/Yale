from collections import defaultdict
def solution(n, costs):
    graph = defaultdict(dict) # Graph
    for n1, n2, cost in costs:
        graph[n1][n2] = cost
        graph[n2][n1] = cost
    V = list(graph.keys()) # Vertexes
    n = len(V)
    Cost = 0
    start = V[0]
    Visited = [start]
    while len(Visited) != n:
        min_dist = 9999
        min_v = -1
        for v1 in Visited:
            for v2 in graph[v1]:
                if v2 not in Visited and graph[v1][v2] < min_dist:
                    min_dist = graph[v1][v2]
                    min_v = v2
        Cost += min_dist
        Visited.append(min_v)
    return Cost