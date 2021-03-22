if __name__ == '__main__':
    n=int(input())
    ans=0
    while (n):
        n=n&(n-1)
        ans+=1

    print(ans)
