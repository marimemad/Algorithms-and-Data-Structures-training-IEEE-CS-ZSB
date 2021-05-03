if __name__ == '__main__':
    digits=list(input())

    n=len(digits)

    i=n-2
    while i>=0 :
        if digits[i]>=digits[i+1]:
            i-=1
        else:
            break

    if i==-1:
        print(-1)

    else:
        j=n-1
        while j>=0:
            if digits[i] >= digits[j]:
                j-=1
            else:
                break

        digits[i] , digits[j] = digits[j] , digits[i]
        print(int(''.join(digits[:i+1]) + ''.join(digits[:i:-1])))
