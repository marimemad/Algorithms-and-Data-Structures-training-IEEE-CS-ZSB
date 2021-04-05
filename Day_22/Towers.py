if __name__ == '__main__':

    n,k=map(int,input().split())
    towers=list(map(int,input().split()))
    modified_tower=[]
    temp_l=None

    for i in range(k):
        highest_tower=towers.index(max(towers))
        lowest_tower=towers.index(min(towers))

        if (highest_tower!=lowest_tower)& (highest_tower!=temp_l) :

            if towers[highest_tower]-towers[lowest_tower]==0:
                break

            towers[highest_tower]-=1
            towers[lowest_tower]+=1
            temp_l=lowest_tower

            modified_tower.append(( highest_tower+1,lowest_tower+1 ))



    print(towers[highest_tower]-towers[lowest_tower],len(modified_tower))

    for ind in modified_tower:
        print(ind[0],ind[1])
