import math

def suker_factorizationL(n) :
    tempN = n
    tempFactoEle = 0
    sqrtNum = n/2
    _factoL = []

    _factoL.append(1)
    if n<=2 :
        return _factoL
    elif n > 2 :
        for i in range(2,sqrtNum+2) :
            if tempN%i==0 :
                _factoL.append(i)

    return _factoL

abundantNL = []
for n in range(2,28123) :
#for n in range(2,13) :
    ssum = 0
    tempL = suker_factorizationL(n)
    for kk in tempL :
        ssum += kk

    if ssum > n :   #abundant number
        abundantNL.append(n)
        print n,"facto =",tempL, ssum

print "abundantNL size = ",len(abundantNL)
baseL = [n for n in range(1,28124)]
print "before cnt = ",len(baseL)

for i in range(len(abundantNL)) :
    for j in range(len(abundantNL)) :
        temp = abundantNL[i]+abundantNL[j]
        if temp > 28123 :
            pass
        else :
            if temp in baseL :
                print "remove num : ",temp,i,j
                baseL.remove(temp)

print "after cnt = ",len(baseL)

lSum = 0
for i in baseL :
    lSum += i

print "answer = ",lSum







    
