import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day3\input.txt'

input = input_parser.get_input_as_lines(file)

sum=0
for line in input:
    arr = list(map(int,list(line)))
    print(arr)
    max = 0
    index=-1
    for i in range(0,len(arr)):
        if arr[i]>max:
            max = arr[i]
            index=i

    leftMax = -1
    for i in range(0,index):
        if arr[i]>leftMax:
            leftMax = arr[i]
    
    rightMax = -1
    for i in range(index+1, len(arr)):
        if arr[i]>rightMax:
            rightMax = arr[i]

    maxValue = 0
    rightMaxValue=  (max*10 + rightMax)
    leftMaxValue = (leftMax*10 + max)
    if leftMax == -1:
        maxValue = rightMaxValue
    elif rightMax == -1:
        maxValue = leftMaxValue
    elif leftMaxValue > rightMaxValue:
        maxValue = leftMaxValue 
    else:
        maxValue = rightMaxValue
    print(maxValue)
    sum+=maxValue
    
print(sum)