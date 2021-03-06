import random


class TSPSampleContainer:
    TSPGraph = []
    population = []

    def __init__(self, populationLimit, graphSize):
        self.populationLimit = populationLimit
        self.graphSize = graphSize
        self.generateGraph()
        self.fillPopulation()

    def generateGraph(self):
        for i in range(self.graphSize):
            self.TSPGraph.append([0] * self.graphSize)
            for j in range(self.graphSize):
                if i != j:
                    self.TSPGraph[i][j] = (random.randint(10, 100000000))
        print("Graph is generated..")
        for i in range(self.graphSize):
            print(self.TSPGraph[i])

    def generateRandomPath(self):
        path = [0] * (self.graphSize + 1)
        finishingNode = 0
        variablesList = [finishingNode]
        path[0] = finishingNode

        for i in range(1, self.graphSize):
            randVal = random.randint(1, self.graphSize - 1)
            while variablesList.__contains__(randVal) == True:
                randVal = random.randint(1, self.graphSize - 1)

            path[i] = randVal
            variablesList.append(randVal)

        path[-1] = finishingNode
        return path

    def fillPopulation(self):
        for i in range(self.populationLimit):
            self.population.append(self.generateRandomPath())
