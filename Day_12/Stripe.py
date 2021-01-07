if __name__=='__main__':
    
    n=int(input())
    strip=list(map(int,input().split()))
    
    summ=[0 for _ in range(n)]
    for i in range(n):
        summ[i]=strip[i]+summ[i-1]
        
    ways=0
    for i in range(n-1):
        if summ[i]==summ[n-1]-summ[i]:
            ways+=1
            
    print(ways)
    
    
#time=o(n)
