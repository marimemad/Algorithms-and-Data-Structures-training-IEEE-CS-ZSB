
if __name__ == '__main__':
    n,k,q=list(map(int,input().split()))
    recipes=[0]*200000
    admissible=[0]*200000

    for i in range(n):
        l,r=list(map(int,input().split()))
        recipes[l]+=1
        recipes[r+1]-=1

    for i in(1,len(recipes)):
        recipes[i]=recipes[i+1]


    for i in range(len(recipes)):
        if recipes[i]>=k:
            admissible[i]=1

    for i in range(q):
        a,b=list(map(int,input().split()))
        print(admissible[b]-admissible[a-1])

    
#time=o(4n)
