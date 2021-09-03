#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the pangrams function below.
def pangrams(s):
    st=string.ascii_lowercase
    for i in set(s.lower()):
        st=st.replace(i,'')
    
    if st:
        return('not pangram')
    else:
        return('pangram')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
 
