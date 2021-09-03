def is_less(ind,a2,a3):
    c=0
    for i in range(len(a2)):
        if a2[i]>ind:
            for j in range(len(a3)):
                if a3[j]>a2[i]:
                    c+=1

    return(c)

if __name__ == '__main__':
    n,k=map(int, input().split())
    a=list( map( int, input().split() ) )

    num_ind={}
    count=0
    for i in range(n):
        if a[i]  in num_ind:
            num_ind[a[i]].append(i)
        else:
            num_ind[a[i]]=[i]

    for i in range(n):
        a1=a[i]
        a2=num_ind.get(a[i]*k,None)
        a3=num_ind.get(a[i]*k*k,None)
        if a2==None or a3==None:
            continue
        else:
            count+=is_less(i,a2,a3)

    print(count)
