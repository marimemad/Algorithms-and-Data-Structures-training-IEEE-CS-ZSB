if __name__=='__main__':

    n,m= map(int,input().split())
    nodes=list(map(int,input().split()))
    max_density=0

    for i in range(m):
        a,b,c = map(int,input().split())
        max_density= max(max_density, (nodes[a-1]+nodes[b-1])/c)

    print(max_density)
