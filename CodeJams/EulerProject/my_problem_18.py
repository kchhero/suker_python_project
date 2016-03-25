import itertools

#line20str = [0]*20
#line20int = [0]*20
maxNum = 5
lineL = [0]*maxNum
lineLint= [0]*maxNum
lineLintCB = [0]*maxNum
index=0
sum = 0

#array save
try :
    with open("my_problem_18_test.txt") as data :
        for line in data :
            lineL[index] = line.strip().split(' ')
            index = index+1
except IOError :
    print "File open error"

k = 0
for i in lineL :
    tempL = []
    for j in i :
        tempL.append(int(j))
        
    lineLint[k] = tempL
    k += 1

lineLintCB = lineLint[:]
#print lineLint
#print lineL[-1]
#print lineL[-1][0:3]

def makeSmallTriangle(count):
    startBellow = count
    reverseIndex = -1
    triang = []
    for i in range(startBellow):        
        triang.append(lineLint[reverseIndex][0:startBellow])
        reverseIndex -= 1
        startBellow -= 1
    
    triang.reverse()
    return triang

def settedEle(dL,depth) :
    startIdx = 1
    minSum = dl[0][0]
    sumMinlocation = []
    
    for i in range(pow(2,depth-1)) :
        minSum += dl[startIdx][i] + dl[startIdx+1][i]) > (dl[reverse][i+1] + dl[reverse-1][i]) :
            removeReady = [reverse,i+1]
        if (dl[reverse][i+1] + dl[reverse-1][i+1]) > (dl[reverse][i+1] + dl[reverse-1][i]) :
        
    
def abcd() :
    #for i in range(3,5+1) :
    for i in range(3,6) :
        triab = makeSmallTriangle(i)
        print triab        
        print "\n"

        settedEle(triab,i)
#        tempSumEle = ssum(triab) 
#        print tempSumEle
abcd()
    




#aa = list(itertools.product(*triab))