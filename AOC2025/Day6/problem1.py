import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day6\input.txt'

input = input_parser.get_input_as_lines(file)


ops = {
    "*": operator.mul,
    "+":operator.add,
}
finalRows = []
for line in input:
    arr=line.split(" ")
    temp=arr
    for i in range(len(arr)-1,-1,-1):
        if arr[i]=="":
            temp.pop(i)
    finalRows.append(temp)
sum = 0
for i in range(0, len(finalRows[0])):
    operator = finalRows[len(finalRows)-1][i]
    val = 0
    if operator == "*":
        val = 1
    opsFunc=ops.get(operator)
    for j in range(0,len(finalRows)-1):
        val = opsFunc(val,int(finalRows[j][i]))
    
    sum+=val
print(sum)