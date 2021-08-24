from TravelingSalesmanProblem import *

# TSP Analysis
testSample = TSPSampleContainer(5, 500)

graph1 = TSPGeneticAlgorithm(testSample)
graph1.process()
print(f"Path: {graph1.bestChromosome}")

x = []
for i in range(len(graph1.paths)):
    x.append(i + 1)

print(f'The best solution is: {graph1.bestScore}')

plt.plot(graph1.paths, x, 'co')
plt.xlabel("Selected path weight")
plt.ylabel("Breeding Amount")
plt.title('Population Selection')
plt.show()
