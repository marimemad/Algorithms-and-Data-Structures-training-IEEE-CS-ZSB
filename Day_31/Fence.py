if __name__ == '__main__':
    n,k=map(int,input().split())
    hights=list(map(int,input().split()))

    s=[]
    s.append(hights[0])
    for i in range(1,n):
        s.append(s[i-1]+hights[i])

    min=s[k-1]
    ind=0
    for i in range(k,n):
        sum=s[i]-s[i-k]
        if sum<min:
            min=sum
            ind=i-k+1

    print(ind+1)




    # initial_sum=sum(hights[0:k])
    # ind=0
    #
    # for i in range(1,n-k+1):
    #     s=sum(hights[i:i+k])
    #
    #     if s<initial_sum:
    #         initial_sum=s
    #         ind=i
    #
    # print(ind+1)
