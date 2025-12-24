import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day7\input.txt'

input = input_parser.get_input_as_str_matrix(file)
visited = [[False for _ in range(0,len(input[0]))] for _ in range(0,len(input))]
pathMathrix = [[0 for _ in range(0,len(input[0]))] for _ in range(0,len(input))]

def checkIsPart(input, visited, i ,j):
    while i>=0:
        if input[i][j] == ".":
            if j+1<len(input[0]) and visited[i][j+1]:
                return True
            if j-1>=0 and visited[i][j-1]:
                return True
        if input[i][j] == "S":
            return True
        if input[i][j] == "^":
            return False
        i-=1
    
    return False


def getPossiblePaths(i, j, pathMatirx, input, visited):
    # print()
    while i<len(input):
        if input[i][j] == "^":
            if visited[i][j]:
                return pathMathrix[i][j]
            leftPath = getPossiblePaths(i,j-1,pathMatirx,input,visited)
            rightPath = getPossiblePaths(i,j+1,pathMathrix,input,visited)
            visited[i][j]= True
            pathMathrix[i][j] = leftPath+rightPath
            return pathMathrix[i][j]
        i+=1
    return 1    

paths= 0
for j in range(0, len(input[1])):
    # print(input[2][j])
    if input[2][j] =="^":
        paths = getPossiblePaths(2,j-1,pathMathrix,input,visited) + getPossiblePaths(2,j+1,pathMathrix,input,visited) 

print(paths)