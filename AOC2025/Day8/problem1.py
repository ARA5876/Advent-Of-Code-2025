import sys 
import os
import math
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day8\input.txt'

def getDistance(i, j, coordinates):
    if i == j:
        return float('inf')
    x1, y1, z1 = coordinates[i]
    x2, y2, z2 = coordinates[j]
    return math.dist([x1, y1, z1], [x2, y2, z2])


def getChain(currentSet,actualSet,connections,value):
    if currentSet == actualSet:
        return actualSet
    finalSet = set()
    for val in value:
        finalSet = finalSet.union(getChain())
                

connections=defaultdict(set)

input = input_parser.get_input_as_lines(file)
coordinates = [list(map(int, line.split(","))) for line in input]

distanceMatrix = [[getDistance(i,j,coordinates) for j in range (0,len(coordinates))]for i in range (0,len(coordinates))]

minDistanceArray = []
for i in range(0,len(distanceMatrix)):
    for j in range(i+1,len(distanceMatrix[i])):
        minDistanceArray.append({distanceMatrix[i][j]: [i,j]})

sorted_data = sorted(minDistanceArray, key=lambda d: list(d.keys())[0])
sorted_data = sorted_data[:1000]
for val in sorted_data:
    myList = list(val.values())[0]
    connections[myList[0]].add(myList[1])
    connections[myList[1]].add(myList[0])

sortedDict = sorted(connections.items())

uniqueSets = []
maxCircuitLength = []
for key,value in sortedDict:
    currentSet = set()
    while currentSet != value :
        currentSet = value
        value = set()
        for val in currentSet:
            value = value.union(connections[val])
        value = value.union(currentSet)
    if not uniqueSets.__contains__(currentSet) :
        uniqueSets.append(currentSet)

sortedUniqueSets = sorted(uniqueSets, key=lambda d: len(d),reverse=True)

print(len(sortedUniqueSets[0])*len(sortedUniqueSets[1])*len(sortedUniqueSets[2]))