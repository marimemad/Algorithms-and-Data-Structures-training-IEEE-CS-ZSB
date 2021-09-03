if __name__ == '__main__':
    matrix=[ input().split() for i in range(5)]
    index_1=tuple()

    for i in range(5):
        for j in range(5):
            if matrix[i][j]=='1':
                index_1=(i,j)
                break

    steps=abs(2-index_1[0]) + abs(2-index_1[1])
    print(steps)
