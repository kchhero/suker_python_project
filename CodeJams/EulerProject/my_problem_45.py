import sys

def getTn(n) :
    return n*(n+1)/2
def getPn(n) :
    return n*(3*n-1)/2
def getHn(n) :
    return n*(2*n-1)

start = 287
pL = [getPn(p) for p in range(1,start)]

for t in range(start,10000000,2) :
    tT = getTn(t)
    hH = t/2
    
    if tT in pL :
        print "Answer :",tT, t, pL.index(tT)+1
        sys.exit()
    else :
        pL.append(getPn(t))

#Answer : 1533776805 55385 16132
