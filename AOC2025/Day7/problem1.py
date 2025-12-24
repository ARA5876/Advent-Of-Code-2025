import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day7\input.txt'

input = input_parser.get_input_as_str_matrix(file)
visited = [[False for _ in range(0,len(input[0]))] for _ in range(0,len(input))]

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


count = 0
for i in range(1, len(input)):
    for j in range(0, len(input[0])):
        if input[i][j] =="^" and checkIsPart(input,visited,i-1,j):
            count+=1
            visited[i][j]=True
print(count)