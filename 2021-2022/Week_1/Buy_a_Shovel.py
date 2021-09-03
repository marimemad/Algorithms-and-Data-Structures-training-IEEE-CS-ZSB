if __name__ == '__main__':
    k,r=input().split()
    min=0
    s=int(k)
    if k[-1]==r or int(k)%10==0:
        print(1)
    else:
        s+=int(k)
        min+=2
        while str(s)[-1]!=r and s%10!=0:
            s+=int(k)
            min+=1
        print(min)
