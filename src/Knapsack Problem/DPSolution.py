
class KnapsackDP:
    itemValues = []
    weights = []
    optimalElements = []

    def __init__(self, KnapsackSample):
        self.itemValues = KnapsackSample.itemValues
        self.weights = KnapsackSample.weights
        self.maxWeight = KnapsackSample.maxWeight
        self.limit = len(self.itemValues)
        self.optimalElements = [0] * self.limit

    def process(self):
        table = [[0 for i in range(self.maxWeight + 1)]
                 for j in range(self.limit + 1)]

        for i in range(self.limit + 1):
            for j in range(self.maxWeight + 1):
                if i == 0 and j == 0:
                    table[i][j] = 0

                elif j - self.weights[i - 1] >= 0:
                    table[i][j] = max(
                        table[i - 1][j],
                        table[i - 1][j - self.weights[i - 1]]
                        + self.itemValues[i - 1])
                else:
                    table[i][j] = table[i - 1][j]

        self.getMaxValue(table)
        self.setOptimalElements(table)

    def getMaxValue(self, table):
        self.optimalSolution = table[self.limit][self.maxWeight]
        print(f'Optimal solution found by DP is: {self.optimalSolution}')

    def setOptimalElements(self, table):
        tempOpt = self.optimalSolution
        tempMaxWeight = self.maxWeight
        for i in range(self.limit, 1, -1):
            if tempOpt > 0:
                if table[i - 1][self.maxWeight] == tempOpt:
                    self.optimalElements[i - 1] = 0

                elif tempMaxWeight >= self.weights[i - 1]:
                    self.optimalElements[i - 1] = 1
                    tempOpt -= self.itemValues[i - 1]
                    tempMaxWeight -= self.weights[i - 1]

                else:
                    self.optimalElements[i - 1] = 0

    def max(self, value1, value2):
        if value1 > value2:
            return value1
        else:
            return value2
