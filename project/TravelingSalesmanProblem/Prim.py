import heapq
import random
import math
import time
import csv

#data_mode = 'Random'
data_mode = 'Load'
csvfile = "TSP1.csv"
height = 500
width = 700
cities = 15
numIterations = 10000000
max_time = 180
edges = []
dicLocations = {}

def calculateDistance(coordinate1, coordinate2):
    distance = math.sqrt(math.pow(coordinate1[0] - coordinate2[0], 2) + math.pow(coordinate1[1] - coordinate2[1], 2))
    return distance

if data_mode == 'Random':
    for itr in range(cities):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        coordinate = [x, y]
        dicLocations[itr] = coordinate
elif data_mode == 'Load':
    with open(csvfile, 'r') as my_csv:
        contents = list(csv.reader(my_csv, delimiter=","))
        for itr in range(len(contents)):
            x , y= contents[itr][0],contents[itr][1]
            dicLocations[itr] = [float(x), float(y)]
        cities = len(contents)

for itr1 in range(len(dicLocations)):
    for itr2 in range(itr1 + 1, len(dicLocations)):
        edges.append([itr1, itr2, calculateDistance(dicLocations[itr1], dicLocations[itr2])])

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

start = time.time()
result = Prim(edges, 0)
elapsedTime = time.time() - start
print ("Routes : %s" %(result[0]))
print ("Distance : ", result[2])
print ("Elapsed time : ", elapsedTime, "secs")