#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    result = 0
    multiplier = 0
    numDigits = len(str(n))
    for i in range(0, numDigits):
        multiplier = (multiplier + (10**i))%(10**9 + 7)
        digit = n % 10
        result = (result + digit*(numDigits-i)*multiplier)%(10**9 + 7)
        n //= 10 
    return (result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n =int(input())

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
