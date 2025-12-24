import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day6\input.txt'


ops = {
    "*": operator.mul,
    "+":operator.add,
}
input = input_parser.get_input_as_lines_without_strip(file)
print(input)


i=len(input[len(input)-1])-1
initialValue=len(input)-1
sum = 0

tempArr = []
while i>=0:
    if input[len(input)-1][i]==" ":
        num = ""
        for j in range(0,len(input)-1):
            if input[j][i]!=" ":
                num+=input[j][i]
        print(num)
        tempArr.append(int(num))
    else: 
        num = ""
        for j in range(0,len(input)-1):
            print(input[j][i])
            if input[j][i]!=" ":
                num+=input[j][i]
        print(num)
        tempArr.append(int(num))

        print(tempArr)


        operator = input[len(input)-1][i]
        val = 0
        if operator == "*":
            val = 1
        opsFunc=ops.get(operator)
        print(operator)
        for num in tempArr:
            val=opsFunc(val,num)
        print(val)
        sum+=val
        tempArr=[]
        i=i-1
    i=i-1

print(sum)