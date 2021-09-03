'''
Sean invented a game involving a 2n *2n  matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the  submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal. 
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingMatrix function below.

#time=o(n^2)
def flippingMatrix(matrix):
    n=len(matrix[0])
    Sum = 0
    for i in range(0, n // 2):  
        for j in range(0, n // 2):  
          
            r1, r2 = i, n - i - 1
            c1, c2 = j, n - j - 1
             
            Sum += max(max(matrix[r1][c1], matrix[r1][c2]),  
                       max(matrix[r2][c1], matrix[r2][c2]))  
          
    return Sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
