#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = list() 
    max_area =0
    index = 0
    
    while index < len(h): 
        if (not stack) or (h[stack[-1]] <= h[index]): 
            stack.append(index) 
            index += 1
            
        else:
            top_of_stack = stack.pop() 
            
            area = (h[top_of_stack] * ((index - stack[-1] - 1)  if stack else index)) 
            max_area = max(max_area, area) 
              
    while stack:
        
        top_of_stack = stack.pop() 
        
        area = (h[top_of_stack] * ((index - stack[-1] - 1)  if stack else index)) 
        max_area = max(max_area, area) 
    
    return max_area 
              
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
 
