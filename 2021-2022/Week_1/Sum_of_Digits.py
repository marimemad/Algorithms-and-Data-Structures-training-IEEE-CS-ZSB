def sum(n):
    s=int(n[0])
    for i in n[1:]:
        s+=int(i)
    return str(s)
if __name__ == '__main__':
    n=input()
    s='0'
    c=0
    if len(n)==1:
        print(0)
    else:
        s=sum(n)
        c+=1
        while len(s)!=1:
            s=sum(s)
            c+=1
        print(c)
