
def binary_to_decimal(n):
    return(int(n,2))



def calc_time(n):
    
    n=binary_to_decimal(n)
    count=0
    t=1
    
    while t<n:
        count+=1
        t*=4
    return(count)



if __name__=='__main__':
    num=input()
    print(calc_time(num))
