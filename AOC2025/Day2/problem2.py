import sys 
import os
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day2\input.txt'

ranges = input_parser.get_input_as_str(file).split(",")
sum = 0
for rang in ranges :
    arr = rang.split("-")
    # if len(arr[0])%2 !=0 and len(arr[1])%2 !=0 and len(arr[0]) == len(arr[1]):
    #     continue
    # print(arr)
    for i in range(int(arr[0]),int(arr[1])+1):
        num = str(i)
        for j in range(1,len(num)//2 + 1):
            tempNum = num[:j]

            temp = num.split(tempNum)
            all_empty = all(not item for item in temp)
            if all_empty :
                print(num)
                sum+=i
                break
        
        # if len(num)%2 == 0 and num[:int(len(num)/2)] == num[int(len(num)/2):] :
        #     sum+=i
        # else:
print(sum)