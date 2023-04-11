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


def substitutePopulation(self, population, children):
    n = len(population)
    new_population = population
    for itr in range(len(children)):
        new_population.append(children[itr])

    for itr1 in range(len(new_population)):
        for itr2 in range(itr1+1,len(new_population)):
            if new_population[itr1].getPhenotype() > new_population[itr2].getPhenotype():
                new_population[itr1], new_population[itr2] = new_population[itr2], new_population[itr1]

    return new_population[:n]

def mutation(self, instance):
    genotype = instance.getGenotype()
    mutationDone = False
    while  mutationDone == False:
        idx1 = -1
        idx2 = -1
        while idx1 == idx2:
            idx1 = random.randint(0, len(genotype)-1)
            idx2 = random.randint(0, len(genotype)-1)
        new_genotype=self.swap_two_cites(instance, idx1, idx2)
        instance.setGenotype(new_genotype)
        mutationDone = self.isInfeasible(genotype)