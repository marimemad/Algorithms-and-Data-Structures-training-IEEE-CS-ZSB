'''
outputstandard output
According to an old legeng, a long time ago Ankh-Morpork residents did something wrong to miss Fortune, and she cursed them. She said that at some time n snacks of distinct sizes will fall on the city, and the residents should build a Snacktower of them by placing snacks one on another. Of course, big snacks should be at the bottom of the tower, while small snacks should be at the top.

Years passed, and once different snacks started to fall onto the city, and the residents began to build the Snacktower.
However, they faced some troubles. Each day exactly one snack fell onto the city, but their order was strange. So, at some days the residents weren't able to put the new stack on the top of the Snacktower: they had to wait until all the bigger snacks fell. Of course, in order to not to anger miss Fortune again, the residents placed each snack on the top of the tower immediately as they could do it.

Write a program that models the behavior of Ankh-Morpork residents.
'''




#time=o(n*m)
def snacktower(array):
    result=[]
    panddind=[]
    maax=max(array)
    
    for i in array:
        
        if i==maax:
            result.append(i)
            maax-=1
            for _ in range(len(panddind)):
                if maax in panddind:
                    result.append(maax)
                    panddind.remove(maax)
                    maax-=1
            
        else:
            result.append('\n')
            panddind.append(i)
            
            
    result=' '.join(list(map(str,result)))
    
    return(result)




if __name__=='__main__':
    n=int(input())
    array=list(map(int,input().split()))
    print(snacktower(array))
    
