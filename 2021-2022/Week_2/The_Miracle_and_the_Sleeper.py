
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        r,l=map(int,input().split())
        print(int(l%max(r,(l//2)+1)))
        
        
#https://codeforces.com/problemset/problem/1562/A
