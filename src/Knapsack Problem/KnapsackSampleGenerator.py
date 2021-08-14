import random


class KnapsackSampleContainer:
    weights = []
    itemValues = []
    population = []
    maxWeight = 0

    def __init__(self, limit):
        self.limit = limit
        self.maxWeight = limit * 10
        self.generateValues()

    def generateValues(self):
        for i in range(self.limit):
            self.weights.append(random.randint(1, 100))
            self.itemValues.append(random.randint(10, 100))

        self.fillPopulation()

    def importSample(self, weights, itemValues, maxWeight):
        self.weights = weights
        self.itemValues = itemValues
        self.maxWeight = maxWeight
        self.fillPopulation()

    def generateRandomChromosome(self):
        newChromosome = [0] * self.limit
        for i in range(self.limit):
            randomGene = random.randint(0, self.limit - 1)
            newChromosome[randomGene] = 1

            currentWeight = self.getTotalWeight(newChromosome, self.weights)
            if currentWeight > self.maxWeight:
                newChromosome[randomGene] = 0
                break

        return newChromosome

    def fillPopulation(self):
        for i in range(20):
            self.population.append(self.generateRandomChromosome())

    def getTotalValue(self, chromosome, itemValues):
        totalValue = 0
        for i in range(len(chromosome)):
            totalValue += chromosome[i] * itemValues[i]

        return totalValue

    def getTotalWeight(self, chromosome, weights):
        totalWeight = 0
        for i in range(self.limit):
            totalWeight += chromosome[i] * weights[i]

        return totalWeight
