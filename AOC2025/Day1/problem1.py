import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day1\input.txt'

lines = input_parser.get_input_as_lines(file)

currentValue = 50
password = 0

for line in lines:
    direction = line[:1]
    value = int(line[1:])
    if direction == 'R':
        currentValue = currentValue+value if currentValue+value<100 else (currentValue+value)%100 
    else:
        currentValue = currentValue-value if currentValue-value>=0 else (currentValue-value)%100
    
    if currentValue == 0 :
        password +=1


print(password)