import sys 
import os
import math
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
import matplotlib.pyplot as plt
import numpy as np
import shapely as sh
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day9\input.txt'
                
def getArea(i,j,coordinates):
    return (abs(coordinates[i][0]-coordinates[j][0]) + 1)*(abs(coordinates[i][1]-coordinates[j][1]) + 1)

input = input_parser.get_input_as_lines(file)
coordinates = [list(map(int, line.split(","))) for line in input]

shape = sh.Polygon(coordinates)

def checkCorner(corner):
    return shape.contains(corner) or shape.touches(corner)

maxArea = 0

for i in range(0, len(coordinates)):
    for j in range(i+1,len(coordinates)):
        corner1 = coordinates[i]
        corner2 = coordinates[j]
        box = sh.box(min(corner1[0],corner2[0]),min(corner1[1],corner2[1]),max(corner1[0],corner2[0]),max(corner1[1],corner2[1]))

        if shape.contains(box):
            area = getArea(i,j,coordinates)
            if area>maxArea: 
                maxArea = area
print(maxArea)