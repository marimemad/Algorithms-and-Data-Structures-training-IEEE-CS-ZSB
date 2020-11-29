#!/bin/python3

import os
import sys
from collections import deque
sys.setrecursionlimit(10000)
#
# Complete the swapNodes function below.
#
class Node: 
  
    # constructor to create a new node   
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        
     
    
def swap(root,k,level,l):
    if root:
        
        if level%k==0:
            root.left ,root.right = root.right, root.left
        
        swap(root.left,k,level+1,l)
        l.append(root.data)
        swap(root.right,k,level+1,l)
        
        
        
def swapNodes(indexes, queries):
    root=Node(1)
    q=deque([root])
    for x,y in indexes:
        temp=q.popleft()
        
        if x!=-1:
            temp.left=Node(x)
            q.append(temp.left)
            
        if y!=-1:
            temp.right=Node(y)
            q.append(temp.right)
            
            
    result=[]
    for k in queries:
        l=[]
        swap(root,k,1,l)
        result.append(l)
        
    return(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
 





















'''
# Python program to swap nodes 
  
# A binary tree node 
class Node: 
  
    # constructor to create a new node   
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# A utility function swap left node and right node of tree 
# of every k'th level  
def swapEveryKLevelUtil(root, level, k): 
      
    # Base Case  
    if (root is None or (root.left is None and
                        root.right is None ) ): 
        return 
  
    # If current level+1 is present in swap vector 
    # then we swap left and right node 
    if (level+1)%k == 0: 
        root.left, root.right = root.right, root.left 
      
    # Recur for left and right subtree 
    swapEveryKLevelUtil(root.left, level+1, k) 
    swapEveryKLevelUtil(root.right, level+1, k) 
  
      
# This function mainly calls recursive function 
# swapEveryKLevelUtil 
def swapEveryKLevel(root, k): 
      
    # Call swapEveryKLevelUtil function with  
    # initial level as 1 
    swapEveryKLevelUtil(root, 1, k) 
  
# Method to find the inorder tree travesal 
def inorder(root): 
      
    # Base Case 
    if root is None: 
        return 
    inorder(root.left) 
    print root.data,  
    inorder(root.right) 
  
# Driver code 
""" 
          1 
        /   \ 
       2     3 
     /      /  \ 
    4      7    8  
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.right.right = Node(8) 
root.right.left = Node(7) 
  
k = 2 
print "Before swap node :" 
inorder(root) 
  
swapEveryKLevel(root, k) 
  
print "\nAfter swap Node : "
inorder(root) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 


'''
