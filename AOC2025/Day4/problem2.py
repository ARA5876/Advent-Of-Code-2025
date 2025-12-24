import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day4\input.txt'

input = input_parser.get_input_as_str_matrix(file)

for line in input:
    print(line)
finalCount = 0

def checkForAdjacentCount(input,i,j):
    num =0
    if i-1>=0 and j-1>=0 and input[i-1][j-1]=='@':
        num+=1
    if i-1>=0 and j+1<len(input[i]) and input[i-1][j+1]=='@' :
        num+=1
    if i-1>=0 and input[i-1][j] == '@':
        num+=1
    
    if i+1<len(input) and j-1>=0 and input[i+1][j-1]=='@':
        num+=1
    if i+1<len(input) and j+1<len(input[i]) and input[i+1][j+1]=='@' :
        num+=1
    if i+1<len(input) and input[i+1][j] == '@':
        num+=1

    if j-1>=0 and input[i][j-1]=='@':
        num+=1
    if j+1<len(input[i]) and input[i][j+1]=='@' :
        num+=1
    
    if num <4:
        print(num)
        return True
    return False



while True:
    count=0
    for i in range(0,len(input)):
        for j in range(0,len(input[i])):
            if input[i][j] == '@' and checkForAdjacentCount(input, i, j):
                input[i][j] = 'X'
                count +=1
    if count == 0:
        break
    finalCount+=count


for line in input:
    print(line)
print(finalCount)
            


# ['.', '.', 'X', 'X', '.', 'X', 'X', '@', 'X', '.']
# ['X', '@', '@', '.', '@', '.', 'X', '.', '@', '@']
# ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@']
# ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.']
# ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@']
# ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@']
# ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@']
# ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@']
# ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.']
# ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.']
