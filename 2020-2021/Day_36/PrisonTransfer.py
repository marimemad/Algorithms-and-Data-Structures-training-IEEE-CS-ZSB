if __name__ == '__main__':
    n,t,c=map(int, input().split())
    prisoners=list(map(int, input().split()))

    result=count=0
    for i in prisoners:
        if i>t:
            count=0
        else:
            count+=1

            if count==c:
                count-=1
                result+=1

    if count==c:
        result+=1
    print(result)










    # result=temp=i=begin=count_c=0
    # while i<n:
    #     if count_c ==c:
    #         result+=1
    #         temp=count_c=0
    #         i=begin+1
    #         begin+=1
    #
    #     else:
    #         if prisoners[i]<=t:
    #             temp+=1
    #             count_c+=1
    #             i+=1
    #         else:
    #             temp=count_c=0
    #             i=begin+1
    #             begin+=1
    #
    # if temp==c:
    #     result+=1
    # print(result)
