
if __name__=='__main__':
    
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    prefix=list()
    
    for i in range(n):
        l.append(len(set(a[i:])))
        
    for i in range(m):
        l=int(input())
        print(prefix[l])

#time=o(n^2)
