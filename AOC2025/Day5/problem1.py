import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day5\input.txt'

input = input_parser.get_input_as_lines(file)

ranges =[]
startNumIndex=0
for i in range(0,len(input)):
    if input[i] == "":
        startNumIndex=i+1
        break
    ranges.append(list(map(int,input[i].split("-"))))
print(ranges)

fresh=0
for j in range(startNumIndex,len(input)):
    num = int(input[j])
    for range in ranges:
        if num>= range[0] and num<=range[1]:
            fresh+=1
            break

print(fresh)