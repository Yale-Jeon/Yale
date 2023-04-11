from GeneticAlgorithmProblem import *
import random
import math
import time
import csv
import numpy as np

class TravelingSalesmanProblem(GeneticAlgorithmProblem):
    
    genes = []
    dicLocations = {}
    gui = ''
    best = ''
    time = 0
    table = {}
    
    def __init__(self, data_mode,csvfile,numCities, height, width, time):
        self.time = time
        if data_mode == 'Random':
            for itr in range(numCities):
                x = random.uniform(0, width)
                y = random.uniform(0, height)
                coordinate = [x, y]
                self.dicLocations[itr] = coordinate
        elif data_mode == 'Load':
            with open(csvfile, 'r') as my_csv:
                contents = list(csv.reader(my_csv, delimiter=","))
                for itr in range(len(contents)):
                    x , y= contents[itr][0],contents[itr][1]
                    self.dicLocations[itr] = [float(x),float(y)]
                    
        for itr1 in range(len(self.dicLocations)):
            for itr2 in range(itr1+1, len(self.dicLocations)):
                self.table[(itr1, itr2)] = self.calculateDistance(self.dicLocations[itr1], self.dicLocations[itr2])
                self.table[(itr2, itr1)] = self.table[(itr1, itr2)]
                
    def registerGUI(self, gui):
        self.gui = gui

    def performEvolution(self, numIterations, numOffsprings, numPopulation, mutationFactor):
        if self.gui != '':
            self.gui.start()
        startTime = time.time()
        population = self.createInitialPopulation(numPopulation, len(self.dicLocations.keys()))
        factor = int(mutationFactor * len(self.dicLocations.keys()))
        while True:
            currentTime = time.time()
            if (currentTime - startTime) >= self.time:
                break
            offsprings = {}
            parents_set = self.selectParents(population, numOffsprings)

            for itr in range(numOffsprings):
                offsprings[itr] = self.crossoverParents(parents_set[itr][0], parents_set[itr][1])
                for i in range(len(self.dicLocations.keys())):
                    x = random.random()
                    if x < mutationFactor:
                        self.mutation(offsprings[itr],factor)

            population = self.substitutePopulation(population, offsprings)
            
            mostFittest = self.findBestSolution(population)
            self.best = mostFittest
            print(self.calculateTotalDistance(self.best))
            if self.gui != '':
                self.gui.update()

        endTime = time.time()
        return self.best.getGenotype(), self.fitness(self.best), self.calculateTotalDistance(self.best), (endTime - startTime)

    def fitness(self, instance):
        distance = self.calculateTotalDistance(instance)
        utility = 10000.0 / distance
        return utility
    
    def calculateTotalDistance(self, instance):
        genotype = instance.getGenotype()
        currentCity = 0
        distance = 0.0
        for itr in range(len(genotype)-1):
            nextCity = genotype[currentCity]
            distance = distance + self.table[(currentCity,nextCity)]
            currentCity = nextCity
        return distance
    
    def calculateDistance(self, coordinate1, coordinate2):
        distance = math.sqrt( math.pow(coordinate1[0]-coordinate2[0], 2) + math.pow(coordinate1[1]-coordinate2[1], 2) )
        return distance

    def getPotentialGenes(self):
        return self.dicLocations.keys()

    def createInitialPopulation(self, numPopulation, numCities):
        population = []
        for itr in range(numPopulation):
            genotype = list(range(numCities))
            while self.isInfeasible(genotype) == False:
                random.shuffle(genotype)
            instance = GeneticAlgorithmInstance()
            instance.setGenotype(genotype)
            population.append(instance)
        return population
        
    def isInfeasible(self, genotype):
        currentCity = 0
        visitedCity = {}
        for itr in range(len(genotype)):
            visitedCity[currentCity] = 1
            currentCity = genotype[currentCity]
            
        if len(visitedCity.keys()) == len(genotype): 
            return True
        else:
            return False
        
    def findBestSolution(self, population):
        idxMaximum = -1
        max = -99999
        for itr in range(len(population)):
            if max < self.fitness(population[itr]):
                max = self.fitness(population[itr])
                idxMaximum = itr
        return population[idxMaximum]

    def selectParents(self, population, numOffsprings):
        rankCost = {}
        originalcost = {}
        BestCost = -999999
        WorstCost = 999999
        for itr in range(len(population)):
            originalcost[itr] = population[itr].getPhenotype()
            if WorstCost < originalcost[itr]:
                WorstCost = originalcost[itr]
            if BestCost > originalcost[itr]:
                BestCost = originalcost[itr]

        size = float(len(population))
        total = 0.0
        for itr in range(len(population)):
            rankCost[itr] = WorstCost - originalcost[itr] + (WorstCost - BestCost) / (size - 1)
            total = total + rankCost[itr]
            
        parents_set=[]
        for itr in range(numOffsprings):
            idx1 = -1
            idx2 = -1
            while idx1 == idx2:
                dart = random.uniform(0, total)
                sum = 0.0
                for itr in range(len(population)):
                    sum = sum + rankCost[itr]
                    if dart <= sum:
                        idx1 = itr
                        break
                dart = random.uniform(0, total)
                sum = 0.0
                for itr in range(len(population)):
                    sum = sum + rankCost[itr]
                    if dart <= sum:
                        idx2 = itr
                        break
            parents_set.append([population[idx1], population[idx2]])
        return parents_set

    def crossoverParents(self, instance1, instance2):
        genotype1 = instance1.getGenotype()
        newInstance = GeneticAlgorithmInstance()
        
        currentCity = 0
        visitedCity = {}
        to_visit=list(range(len(genotype1)))
        child = {}
        
        for i in range(len(genotype1)):
            visitedCity[currentCity] = 1
            to_visit.remove(currentCity)
            if len(to_visit) == 0:
                child[currentCity] =0
            else:
                Cities = self.getNeighborCity(instance1, currentCity) + self.getNeighborCity(instance2, currentCity)
                minimum = 99999
                minCity = None
                for city in Cities:
                    if self.table[currentCity, city] < minimum:
                        if city not in visitedCity:
                            minimum = self.table[currentCity, city]
                            minCity = city
                if minCity == None:
                    minimum = 99999
                    for nextCity in to_visit:
                        if self.table[currentCity, nextCity] < minimum:
                            minimum = self.table[currentCity, nextCity]
                            minCity = nextCity

                child[currentCity] = minCity
                currentCity = minCity
                
        genotype = []
        for itr in range(len(child)):
            genotype.append(child[itr])
            
        newInstance.setGenotype(genotype)
        return newInstance
        
            
    
    def getMinimumNeighborNotVisitedCity(self, lstVisitedCity, dicNeighbor):
        cities = list(dicNeighbor.keys())
        for itr in range(len(lstVisitedCity)):
            cities.remove(lstVisitedCity[itr])
        minimum = 999
        candidates = []
        for itr in range(len(cities)):
            location = cities[itr]
            if len(dicNeighbor[location]) <= minimum:
                minimum = len(dicNeighbor[location])
                candidates.append(location)
        random.shuffle(candidates)
        if len(candidates) == 0:
            return -1
        return candidates[0]
        
    def getNeighborCity(self, instance, currentCity):
        
        genotype = instance.getGenotype()
        ret1 = -1
        ret2 = -1
        for itr in range(len(genotype)):
            if genotype[itr] == currentCity:
                ret1 = itr
                break
        ret2 = genotype[currentCity]
        neighbor = [ret1, ret2]
        return neighbor

    def mutation(self, instance, factor):
        genotype = instance.getGenotype()
        mutationDone = False
        while mutationDone == True:
            for itr in range(factor):
                idxSwap1 = random.randint(0, len(genotype))
                idxSwap2 = random.randint(0, len(genotype))
                genotype[idxSwap1], genotype[idxSwap2] = genotype[idxSwap2], genotype[idxSwap1]
            if self.isInfeasible(genotype) == True:
                mutationDone = False
            else:
                mutationDone = True
        instance.setGenotype(genotype)

    def swap_two_cites(self, instance, idx1, idx2):
        genotype = instance.getGenotype()
        new_genotype = {}
        
        if genotype[idx1] == idx2:
            before = self.getNeighborCity(instance, idx1)[0]
            after = genotype[idx2]
            genotype[before] = idx2
            genotype[idx2] = idx1
            genotype[idx1] = after
            
        elif genotype[idx2] == idx1:
            before = self.getNeighborCity(instance, idx2)[0]
            after = genotype[idx1]
            genotype[before] = idx1
            genotype[idx1] = idx2
            genotype[idx2] = after
        
        else:  
            beforecity = self.getNeighborCity(instance, idx1)[0]
            currentcity = idx1
            
            while currentcity != idx2:
                nextcity = genotype[currentcity]
                new_genotype[nextcity] = currentcity
                currentcity = nextcity
    
            new_genotype[idx1] = genotype[idx2]
            new_genotype[beforecity] = idx2
            
            for itr in new_genotype:
                genotype[itr] = new_genotype[itr]
            
        return genotype

    def substitutePopulation(self, population, children):
        for itr1 in range(len(population)):
            for itr2 in range(itr1+1,len(population)):
                if self.fitness(population[itr1]) < self.fitness(population[itr2]):
                    population[itr1], population[itr2] = population[itr2], population[itr1]
        for itr in range(len(children)):
            population[len(population)-len(children)+itr] = children[itr]
        return population