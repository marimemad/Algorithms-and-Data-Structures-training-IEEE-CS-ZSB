def tower_builder(n_floors):
    tower = []
    asterisk = 1
    space = (2*(n_floors - 1) + 1)//2
    
    for i in range(n_floors):
        tower.append(space*' ' + '*'*asterisk + space*' ')
        asterisk += 2
        space -= 1
    
    return(tower)
