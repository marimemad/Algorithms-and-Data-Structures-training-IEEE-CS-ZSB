if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n,a,b=list(map(int,input().split()))
        s=input()
        c=1
        for j in range(n-1):
            if s[j]!=s[j+1]:
                c+=1
        print(n*a + max(n*b,b*(c//2 + 1 )))
        
#https://codeforces.com/problemset/problem/1550/B
