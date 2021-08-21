from TSPSampleGenerator import *
import random
import math
import matplotlib.pyplot as plt


class TSPGeneticAlgorithm():
    paths = []
    bestChromosome = []
    bestScore = 0

    def __init__(self, TSPSample):
        self.TSPSample = TSPSample

    def process(self):
        self.TSPGraph = self.TSPSample.TSPGraph
        self.population = self.TSPSample.population
        self.selection()

        for i in self.population:
            self.calculatePathWeight(i)

    def selection(self):
        chromosome1 = self.population[0].copy()
        chromosome2 = self.population[1].copy()
        selection = Selection(self.TSPGraph)
        selection.breedingLoop(chromosome1, chromosome2)
        self.bestChromosome = selection.bestChromosome
        self.bestScore = selection.bestScore

    def calculatePathWeight(self, path):
        totalWeight = 0
        previousNode = 0  # finishing node
        for node in path:
            totalWeight += self.TSPGraph[previousNode][node]
            previousNode = node

        return totalWeight


# Selection class handles selective breeding. We put two
# good chromosomes into breeding loop and in every cycle
# the chromosomes create new baby chromosomes. After each
# breeding cycle we control if they are better from their
# parents or not. If so, then we select them for the next cycle.


class Selection(TSPGeneticAlgorithm):

    def __init__(self, TSPGraph):
        self.TSPGraph = TSPGraph

    def breedingLoop(self, chromosome1, chromosome2):
        iteration = 0
        while iteration < 20000:
            temp1 = chromosome1.copy()
            temp2 = chromosome2.copy()

            chromosome1, chromosome2 = self.crossover(
                chromosome1, chromosome2)

            chromosome1 = self.selectiveBreeding(
                chromosome1, temp1)
            chromosome2 = self.selectiveBreeding(
                chromosome2, temp2)

            if iteration % 1000 == 0:
                self.printValues(chromosome1, chromosome2)

            self.paths.append(self.calculatePathWeight(chromosome1))
            iteration += 1

    def crossover(self, chromosome1, chromosome2):
        chromosomeLenght = len(chromosome1)
        for i in range(math.floor(chromosomeLenght / 2)):
            randomIndex = random.randint(1, chromosomeLenght - 1)
            swapGenes(chromosome1, chromosome2, randomIndex)

            chromosome1 = Mutation().igniteMutation(chromosome1)
            chromosome2 = Mutation().igniteMutation(chromosome2)

        return chromosome1, chromosome2

    def selectiveBreeding(self, babyChromosome, chromosome):
        babyChromosomeScore = self.calculatePathWeight(babyChromosome)
        chromosomeScore = self.calculatePathWeight(chromosome)

        if babyChromosomeScore < chromosomeScore:
            return babyChromosome
        else:
            return chromosome

    def printValues(self, chromosome1, chromosome2):
        val1 = self.calculatePathWeight(chromosome1)

        val2 = self.calculatePathWeight(chromosome2)

        if val1 < val2:
            self.bestChromosome = chromosome1
            self.bestScore = val1
        else:
            self.bestChromosome = chromosome2
            self.bestScore = val2

        # print(self.bestChromosome)
        print(f'{self.bestScore}')


# Mutation class randomly swaps the genes inside of
# the given chromosome and this causes variation we need.

class Mutation:
    def __init__(self):
        pass

    def igniteMutation(self, chromosome):
        tempChromosome = chromosome
        if random.randint(0, 100) < 50:
            tempChromosome = self.mutationCycle(chromosome).copy()

        return tempChromosome

    def mutationCycle(self, chromosome):
        tempChromosome = chromosome.copy()
        chromosomeLenght = len(tempChromosome)

        randomIndex1 = random.randint(1, chromosomeLenght - 2)
        randomIndex2 = random.randint(1, chromosomeLenght - 2)

        tempGene = tempChromosome[randomIndex1]
        tempChromosome[randomIndex1] = tempChromosome[randomIndex2]
        tempChromosome[randomIndex2] = tempGene

        return tempChromosome

# This algorithm is a little weird but since it is trivial,
# we can use any random swapping algorithm for this case.


def swapGenes(chromosome1, chromosome2, index):
    tempGene = chromosome1[index]
    chromosome1[index] = chromosome2[index]
    chromosome2[index] = tempGene

    tempGene = chromosome1[index]
    for i in range(1, len(chromosome1) - 1):
        if i != index and tempGene == chromosome1[i]:
            tempGene = chromosome2[index]
            for j in range(1, len(chromosome2) - 1):
                if j != index and tempGene == chromosome2[j]:
                    tempGene = chromosome1[i]
                    chromosome1[i] = chromosome2[j]
                    chromosome2[j] = tempGene
