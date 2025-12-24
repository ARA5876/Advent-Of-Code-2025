import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day5\input.txt'

input = input_parser.get_input_as_lines(file)

ranges =[]
for i in range(0,len(input)):
    if input[i] == "":
        break
    ranges.append(list(map(int,input[i].split("-"))))
print(ranges)

fresh=0


ranges.sort(key=lambda x: x[0])
i=0
while i in range(0,len(ranges)):
    currentRange = ranges[i]
    max=currentRange[1]
    # print(currentRange)
    while i<len(ranges) and ranges[i][0]<=max:
        if ranges[i][1]>max:
            max=ranges[i][1]
        i+=1

    fresh += max-currentRange[0] + 1

print(fresh)