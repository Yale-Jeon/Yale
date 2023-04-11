from Graph import DenseGraph
import csv

def performPrim(graph, src):
    Vertexes = graph.vertexes
    visited=[]
    Edge = {}
    path = {}
    routes = {}
    visited.append(src)
    while visited != Vertexes:
        min_weight = 999999
        min_edge = None
        for vertex in visited:
            edges, weights = graph.getNeighbors(vertex)
            for itr in range(len(edges)):
                if edges[itr] not in visited:
                    if weights[itr] < min_weight:
                        min_weight = weights[itr]
                        min_edge = vertex, edges[itr]
        path[min_edge[1]] = min_edge[0]
        visited.append(edges[itr])
        Edge[min_edge[0]] = {}
        Edge[min_edge[0]][min_edge[1]] = weights[itr]
    
    for vertex in Vertexes:
        next = vertex
        temp = [next]
        while next != src:
            next = path[next]
            if next == None:
                temp = None
                break
            temp = [next] + temp
        routes[vertex] = temp
        
    return visited, Edge, routes