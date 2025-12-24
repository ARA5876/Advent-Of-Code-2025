import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day3\input.txt'

input = input_parser.get_input_as_lines(file)

sum=0

def getMaxValue(arr,active, remaining, start, end):
    if remaining == 0:
        return
    max = 0
    index = 0
    for i in range(start,end):
        if arr[i]>max:
            max = arr[i]
            index=i
    active[index] = True
    remaining-=1
    if end-1-index <= remaining : 
        remaining-= end-index-1
        for i in range(index+1,end):
            active[i]= True

        getMaxValue(arr,active,remaining,start,index)
    else :
        getMaxValue(arr, active, remaining, index+1,end)




for line in input:
    arr = list(map(int,list(line)))
    active = [False]*len(arr)
    getMaxValue(arr,active,12,0,len(arr))

    maxValue=""
    for i in range(0,len(arr)):
        if active[i] :
            maxValue+=str(arr[i])
            
    sum+=int(maxValue)
    
print(sum)


