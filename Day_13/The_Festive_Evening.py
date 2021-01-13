def if_unguarded(n,k,guest):
    last_guest=dict()
    open_gate=set()

    #last guest for each gate
    for i in range(n):
        last_guest[guest[i]]=i

    #if number of open gates > number of guards
    for i in range(n):
        open_gate.add(guest[i])
        if len(open_gate)>k:
            return('YES')
        if i==last_guest[guest[i]]:
            open_gate.remove(guest[i])

    #gates still open >number of guards
    if len(open_gate)<=k:
        return('NO')


if __name__=='__main__':
    n,k=list (map(int,input().split() ))
    guest=input()
    print(if_unguarded(n,k,guest))
