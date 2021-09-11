for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    b=sorted([l[i],i] for i in range(n))
    c=0
    for i in range(1,n):
        if b[i][1]!=b[i-1][1]+1:
            c+=1

    if c<k:
        print("YES")
    else:
        print("NO")

#https://codeforces.com/problemset/problem/1557/B
