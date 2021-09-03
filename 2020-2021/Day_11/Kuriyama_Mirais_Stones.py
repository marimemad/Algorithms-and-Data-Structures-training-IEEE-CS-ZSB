 
if __name__=='__main__':
    
    n=int(input())
    v=list(map(int,input().split()))
    
    v_sorted=sorted(v)
    
    for i in range(1,n):
        v[i]+=v[i-1]
        v_sorted[i]+=v_sorted[i-1]
        
    m=int(input())
    for i in range(m):
        typee,l,r=(map(int,input().split()))
        if typee==1:
            if l==1:
                print(v[r-1])
            else:
                print(v[r-1]-v[abs(l-2)])
            
        else:
            if l==1:
                print(v_sorted[r-1])
            else:
                print(v_sorted[r-1]-v_sorted[abs(l-2)])
                
                
                
                
                
#time=o(n)
