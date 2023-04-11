from TravelingSalesmanProblem import *

#data_mode = 'Random'
data_mode = 'Load'
csvfile = "TSP1.csv"
height = 500
width = 700
cities = 15
numIterations = 100
numOffsprings = 450
numPopulation = 500
mutationFactor = 0.9
time = 180

tsp = TravelingSalesmanProblem(data_mode,csvfile,cities,height, width, time)
routes, utility, distance, elapsedTime = tsp.performEvolution(numIterations, numOffsprings, numPopulation, mutationFactor)

currentCity = 0
route = ''
for itr in range(len(routes)):
    route = route + '->' + str(currentCity)
    currentCity = routes[currentCity]
print ("Routes : %s" %(route))
print ("Distance : ", distance)
print ("Elapsed time : ", elapsedTime, "secs")