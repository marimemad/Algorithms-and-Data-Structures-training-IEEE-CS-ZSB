if __name__=='__main__':
    n=input()
    dog=input()
    
    frequency=[0 for i in range(ord(max(dog))-96)]
    
    for i in dog:
        frequency[ord(i)-97]+=1

    flag=0
    for i in frequency:
        if i>=2 or n==1:
            flag=1
            break
    
    if flag:
        print("YES")  
    else:
        print("NO")
        
#time=o(n)

