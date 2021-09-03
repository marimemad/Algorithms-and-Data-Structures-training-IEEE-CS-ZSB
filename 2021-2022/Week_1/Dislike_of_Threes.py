if __name__ == '__main__':
    like=[]
    for i in range(1, 1667):
        if i % 3 != 0 and i % 10 != 3:
            like.append(i)
    t= int(input())
    for i in range(t):
        k= int(input())
        print(like[k-1])
