if __name__ == '__main__':
    n,f=map(int,input().split())
    k_l=[]
    diff=[]
    sells=0

    for i in range (n):
        ki,li=map(int,input().split())
        k_l.append((ki,li))

        mini=min(ki,li)
        diff.append((2*mini-mini,i))

    diff.sort(reverse=True)

    for d,i in diff:
        if f>0:
            sells+=min(2*k_l[i][0],k_l[i][1])
            f-=1
        else:
            sells+=min( k_l[i][0], k_l[i][1])

    print(sells)
