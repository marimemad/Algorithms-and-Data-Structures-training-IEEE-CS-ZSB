if __name__ == '__main__':

    n, q = map(int,input().split())
    s = input()
    c = [0]
    for i in range(n):
        c.append(c[-1]+ord(s[i])-96)
    for i in range(q):
         l, r = map(int,input().split())
         print (c[r]-c[l-1])
