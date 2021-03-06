
'''
A left rotation operation on an array of size m shifts each of the array's elements 1 unit to the left. Given an integer, , rotate the array that many steps left and return the result.
d=2
arr=[1,2,3,4,5]

[3,4,5,1,2]
'''



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
 #time=o(n)
def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        temp=arr.pop(0)
        arr.append(temp)
    return(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
