
class KnapsackGreedyMethod:
    greedyChromosome = []
    densities = []
    maxValue = 0

    def __init__(self, KnapsackSample):
        self.itemValues = KnapsackSample.itemValues
        self.weights = KnapsackSample.weights
        self.maxWeight = KnapsackSample.maxWeight
        self.limit = len(self.itemValues)

    def process(self):
        self.calculateItemsDensity()
        self.greedilyChoose()
        self.getFinalValues()

    def calculateItemsDensity(self):
        for i in range(self.limit):
            density = self.itemValues[i] / self.weights[i]
            self.densities.append(density)

        self.greedyChromosome = [0] * self.limit

    def greedilyChoose(self):
        while len(self.densities) != 0:
            maxIndex = self.densities.index(max(self.densities))
            self.greedyChromosome[maxIndex] = 1
            self.densities.pop(maxIndex)

            totalWeight = self.getTotalWeight(self.greedyChromosome)
            if totalWeight > self.maxWeight:
                self.greedyChromosome[maxIndex] = 0

    def getTotalWeight(self, chromosome):
        totalWeight = 0
        for i in range(self.limit):
            totalWeight += chromosome[i] * self.weights[i]

        return totalWeight

    def getFinalValues(self):
        print("Greedy Method: ")
        totalWeight = 0

        for i in range(self.limit):
            self.maxValue += self.greedyChromosome[i] * self.itemValues[i]
            totalWeight += self.greedyChromosome[i] * self.weights[i]

        print(f'Max value: {self.maxValue}, total weight: {totalWeight}')
