# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    while root:
        if root.info>v1 and root.info>v2:
            root=root.left
            
        elif root.info<v1 and root.info<v2:
            root=root.right
        
        else:
            break
            
    return(root)
