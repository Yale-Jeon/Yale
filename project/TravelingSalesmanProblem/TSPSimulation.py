from TravelingSalesmanProblem_ori import *

#data_mode = 'Random'
data_mode = 'Load'
csvfile = "TSP1.csv"
height = 500
width = 700
cities = 15
numIterations = 100
numOffsprings = 70
numPopulation = 100
mutationFactor = 0.2
time = 180

table=[]
avg=0.0
for i in range(5):
    tsp = TravelingSalesmanProblem(data_mode,csvfile,cities,height, width, time)
    routes, utility, distance, elapsedTime = tsp.performEvolution(numIterations, numOffsprings, numPopulation, mutationFactor)
    print(distance)
    table.append(distance)
    avg = avg + distance
print('best = ', min(table))
print('average = ',avg/5)


currentCity = 0
route = ''
for itr in range(len(routes)):
    route = route + '->' + str(currentCity)
    currentCity = routes[currentCity]
print ("Routes : %s" %(route))
print ("Distance : ", distance)
print ("Elapsed time : ", elapsedTime, "secs")