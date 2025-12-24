import sys 
import os
import math
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day9\input.txt'
                
def getArea(i,j,coordinates):
    return abs(coordinates[i][0]-coordinates[j][0] + 1)*abs(coordinates[i][1]-coordinates[j][1] + 1)

input = input_parser.get_input_as_lines(file)
coordinates = [list(map(int, line.split(","))) for line in input]

maxArea = 0
for i in range(0, len(coordinates)):
    for j in range(i,len(coordinates)):
        area = getArea(i,j,coordinates)
        if i!=j and area>maxArea:
            maxArea = area
print(maxArea)