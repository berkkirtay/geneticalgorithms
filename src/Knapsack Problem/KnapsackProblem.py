import random
import math


class KnapsackGeneticAlgorithm():
    selectedPopulationScores = []
    bestScore = 0
    bestChromosome = []

    def __init__(self, knapsackSample):
        self.knapsackSample = knapsackSample
        self.population = knapsackSample.population
        self.sampleImport(knapsackSample.weights,
                          knapsackSample.itemValues,
                          knapsackSample.maxWeight)

    def sampleImport(self, weights, itemValues, maxWeight):
        self.weights = weights
        self.itemValues = itemValues
        self.maxWeight = maxWeight

    def process(self):
        self.selection(self.population)

    def selection(self, population):
        chromosomeScores = []
        for i in range(len(population)):
            chromosomeScores.append(self.getTotalValue(
                population[i], self.itemValues))

        maxIndex1 = chromosomeScores.index(max(chromosomeScores))
        chromosomeScores.pop(maxIndex1)

        maxIndex2 = chromosomeScores.index(max(chromosomeScores))
        chromosomeScores.pop(maxIndex2)

        chromosome1 = population[maxIndex1].copy()
        chromosome2 = population[maxIndex2].copy()
        selection = Selection(self.knapsackSample)
        selection.breedingLoop(chromosome1, chromosome2)
        self.bestChromosome = selection.bestChromosome
        self.bestScore = selection.bestScore

    def boundaryCheck(self, chromosome):
        currentWeight = self.getTotalWeight(
            chromosome, self.weights)
        if currentWeight > self.maxWeight:
            return False
        return True

    def getTotalValue(self, chromosome, itemValues):
        totalValue = 0
        for i in range(len(chromosome)):
            totalValue += chromosome[i] * itemValues[i]

        return totalValue

    def getTotalWeight(self, chromosome, weights):
        totalWeight = 0
        for i in range(len(chromosome)):
            totalWeight += chromosome[i] * weights[i]

        return totalWeight

    def printValues(self, chromosome1, chromosome2):

        val1 = self.getTotalValue(chromosome1, self.itemValues)

        val2 = self.getTotalValue(chromosome2, self.itemValues)

        if val1 > val2:
            self.bestChromosome = chromosome1
            self.bestScore = val1
        else:
            self.bestChromosome = chromosome2
            self.bestScore = val2

        print(f'{self.bestScore}')


# Selection class handles selective breeding. We put two
# good chromosomes into breeding loop and in every cycle
# the chromosomes create new baby chromosomes. After each
# breeding cycle we control if they are better from their
# parents or not. If so, then we selec them for the next cycle.


class Selection(KnapsackGeneticAlgorithm):
    def __init__(self, KnapsackSample):
        self.weights = KnapsackSample.weights
        self.itemValues = KnapsackSample.itemValues
        self.maxWeight = KnapsackSample.maxWeight

    def breedingLoop(self, chromosome1, chromosome2):
        iteration = 0
        while iteration < 10000:
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
            iteration += 1

    def crossover(self, chromosome1, chromosome2):
        chromosomeLenght = len(chromosome1)
        for i in range(math.floor(chromosomeLenght / 5)):
            randomIndex = random.randint(0, chromosomeLenght - 1)
            swapGenes(chromosome1, chromosome2, randomIndex)

            if self.boundaryCheck(chromosome1) == False or self.boundaryCheck(chromosome2) == False:
                swapGenes(chromosome1, chromosome2, randomIndex)

        tempChromosome1 = Mutation().igniteMutation(chromosome1)
        tempChromosome2 = Mutation().igniteMutation(chromosome1)

        if self.boundaryCheck(tempChromosome1) == True:
            chromosome1 = tempChromosome1
        if self.boundaryCheck(tempChromosome2) == True:
            chromosome2 = tempChromosome2

        return chromosome1, chromosome2

    def selectiveBreeding(self, babyChromosome, chromosome):
        babyChromosomeScore = self.getTotalValue(
            babyChromosome, self.itemValues)
        chromosomeScore = self.getTotalValue(
            chromosome, self.itemValues)

        self.selectedPopulationScores.append(babyChromosomeScore)

        if babyChromosomeScore > chromosomeScore:
            return babyChromosome
        else:
            return chromosome


# Mutation class randomly swaps the genes inside of
# the given chromosome and this causes variation we need.

class Mutation:
    def __init__(self):
        pass

    def igniteMutation(self, chromosome):
        tempChromosome = chromosome
        if random.randint(0, 100) < 60:
            tempChromosome = self.mutationCycle(chromosome).copy()

        return tempChromosome

    def mutationCycle(self, chromosome):
        tempChromosome = chromosome.copy()
        chromosomeLenght = len(tempChromosome)

        randomIndex1 = random.randint(0, chromosomeLenght - 2)
        randomIndex2 = random.randint(0, chromosomeLenght - 2)

     #   tempGene = tempChromosome[randomIndex1]
      #  tempChromosome[randomIndex1] = tempChromosome[randomIndex2]
       # tempChromosome[randomIndex2] = tempGene
        tempChromosome[randomIndex1] = 1
        tempChromosome[randomIndex2] = 0

        return tempChromosome


def swapGenes(chromosome1, chromosome2, index):
    tempGene = chromosome1[index]
    chromosome1[index] = chromosome2[index]
    chromosome2[index] = tempGene
