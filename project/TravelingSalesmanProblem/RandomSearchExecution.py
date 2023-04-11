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
table = {}
dicLocations = {}

def calculateTotalDistance(instance):
    distance = 0.0
    for itr in range(len(instance) - 1):
        distance = distance + table[(instance[itr], instance[itr+1])]
    return distance

def calculateDistance(coordinate1, coordinate2):
    distance = math.sqrt(math.pow(coordinate1[0] - coordinate2[0], 2) + math.pow(coordinate1[1] - coordinate2[1], 2))
    return distance

def make_solution(cities):
    ret = []
    a = list(range(cities))
    for i in range(cities):
        x = random.randint(1, cities-i)
        ret.append(a.pop(x-1))
    return ret

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
        table[(itr1, itr2)] = calculateDistance(dicLocations[itr1], dicLocations[itr2])
        table[(itr2, itr1)] = table[(itr1, itr2)]

best_solution = ''
best_value = 999999
startTime = time.time()
n = 0
while True:
    currentTime = time.time()
    if (currentTime - startTime) >= max_time or n > numIterations:
        break
    solution = make_solution(cities)
    value = calculateTotalDistance(solution)
    if value < best_value:
        best_value = value
        best_solution = solution
    n += 1
endTime = time.time()
elapsedTime = endTime - startTime

print("Routes : %s" %(best_solution))
print("Distance : ", best_value)
print("Elapsed time : ", elapsedTime, "secs")
