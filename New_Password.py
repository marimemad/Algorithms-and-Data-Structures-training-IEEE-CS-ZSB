'''
Innokentiy decides to change the password in the social net "Contact!", but he is too lazy to invent a new password by himself. That is why he needs your help.

Innokentiy decides that new password should satisfy the following conditions:

the length of the password must be equal to n,
the password should consist only of lowercase Latin letters,
the number of distinct symbols in the password must be equal to k,
any two consecutive symbols in the password must be distinct.
Your task is to help Innokentiy and to invent a new password which will satisfy all given conditions.

Input
The first line contains two positive integers n and k (2 ≤ n ≤ 100, 2 ≤ k ≤ min(n, 26)) — the length of the password and the number of distinct symbols in it.

Pay attention that a desired new password always exists.

Output
Print any password which satisfies all conditions given by Innokentiy.

'''
import re
import random
import string


def creat_paswword(n,k):
    
    lowercase=string.ascii_lowercase
    password=[ random.choice(lowercase) for i in range(k)]
    
    password=list(set(password))
    
    for i in range(k-len(password)):
        temp=random.choice(lowercase)
        
        while temp in password:
            temp=random.choice(lowercase)
            
        password.append(temp)
    
    
    for i in range(n-k):
        password.append(password[i])
    
        
    return(password)





if __name__=='__main__':
    n,k=list(map(int,input().split()))
    print(creat_paswword(n,k))
    
    
    
