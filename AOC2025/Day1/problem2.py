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
    if value>99 :
        password += value//100
        value = value%100
    if direction == 'R':
        tempValue = currentValue + value
        if tempValue>100:
            password += 1    
        currentValue = (tempValue)%100 
    else:
        tempValue = currentValue-value
        if tempValue<0 and currentValue>0: 
            password += 1 
        currentValue = (tempValue)%100
    if currentValue == 0 :
        password +=1


print(password)