
if __name__ == '__main__':
    my_name=input()
    n_actions=int(input())
    priority={'posted':15 , 'commented':10 , 'likes':5}

    names={}
    for i in range(n_actions):
        action= input().split()
        n1,n2=action[0],action[-2][:-2]

        if n1==my_name:
            names.setdefault(n2,0)
            names[n2]-=priority[action[1]]

        elif n2==my_name:
            names.setdefault(n1,0)
            names[n1]-=priority[action[1]]

        else:
            names.setdefault(n1,0)
            names.setdefault(n2,0)

    names=sorted ((v,k) for (k,v) in names.items() )
    for name in names:
        print(name[1])
