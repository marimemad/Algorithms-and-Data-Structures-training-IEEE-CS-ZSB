
if __name__ == '__main__':
    n,m,k=map(int,input().split())
    players=[]
    frinds=0
    for i in range(m+1):
        players.append(int(input()))

    for i in range(m):
        test=players[i]^players[-1]
        cont_1=0
        while (test):
            test=test&(test-1)
            cont_1+=1

        if cont_1<=k:
            frinds+=1
    print(frinds)
