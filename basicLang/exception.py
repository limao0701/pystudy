def conflict(stat,x):
    y=len(stat)
#    if not y:return True
    for i in range(y):
        if abs(stat[i]-x) in (0,y-i):
            return True
    return False

def quen(quens=4,stat=()):
    if len(stat)==quens-1:
        for x in range(quens):
            if not conflict(stat,x):
                yield (x,)
    else:
        for q in range(quens):
            if not conflict(stat,q):
                print stat,q
                for result in quen(quens,stat + (q,)):
                    yield (q,) + result

def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,)+result

#print conflict((),0)
list(queens(4))
                       
#list(quen(8))


        
    

        
