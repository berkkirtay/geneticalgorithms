from KnapsackSampleGenerator import *
from KnapsackProblem import *
from GreedyAlgorithm import *

import matplotlib.pyplot as plt

# Knapsack Problem Analysis

#itemValues = [5, 100, 40, 35, 34, 92, 32, 36, 150, 77]
#weights = [12, 219, 311, 122, 34, 53, 321, 12, 66, 190]

sampleSize = 100
newSample = KnapsackSampleContainer(sampleSize)

# Greedy Method for Knapsack Problem

greedyMethod = KnapsackGreedyMethod(newSample)
greedyMethod.process()


def sortPopulationByScore(population, limit):
    print("Population scores after greedy method.")

    populationScores = []
    for i in range(limit):
        chromosomeScore = newSample.getTotalValue(
            population[i], newSample.itemValues)
        populationScores.append(chromosomeScore)

    list.sort(populationScores)
    print(populationScores)


sortPopulationByScore(newSample.population, len(newSample.population))
print("****************************************************")


# Genetic Method

genetic = KnapsackGeneticAlgorithm(newSample)

genetic.process()


def validateGenes(weights, chromosome, maxWeight):
    totalWeight = 0
    for i in range(len(weights)):
        totalWeight += weights[i] * chromosome[i]

    if totalWeight > maxWeight:
        return False

    print(f"The best chromosomes weight is {totalWeight}")
    return True


validateGenes(newSample.weights, genetic.bestChromosome,
              newSample.maxWeight)

print(f'\n The best found score is : {genetic.bestScore}')

populationScores = genetic.selectedPopulationScores

x = []
for i in range(len(populationScores)):
    x.append(i + 1)


plt.plot(populationScores, x)
plt.plot(greedyMethod.maxValue, 1, 'ro')
plt.xlabel("Item Values")
plt.ylabel("Breeding Amount")
plt.title('Population Selection')
plt.show()
