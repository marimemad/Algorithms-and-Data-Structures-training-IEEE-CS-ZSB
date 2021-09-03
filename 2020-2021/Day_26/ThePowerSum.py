#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N,e):
    value=X-e**N
    if value < 0:
        return 0
    elif value == 0:
        return 1
    else:
        return powerSum(value, N,e+1) + powerSum(X, N,e+1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N,1)

    fptr.write(str(result) + '\n')

    fptr.close()
 
