import math
import sys
#1487,4817,8147

def suker_isPrimeNum(n) :
    if n==2 or n==3 or n==5 or n==7 :
        return 1
    elif n%2==0 :
        return 0
    else :
        sqrtNum = int(math.sqrt(n))        
        for i in xrange(3,sqrtNum+1) :
            if n%i==0 :
                return 0

        return 1

#step1 : primeNum

primeL = []
for i in xrange(1001,9999,2) :
    if suker_isPrimeNum(i)==1 :
        primeL.append(str(i))
        
#step2 : stepNumber
lenPrimeL = len(primeL)

for i, tempA in enumerate(primeL) :
    compareL = []
    compareL.append(tempA)    
    for j in range(i+1,lenPrimeL) :    
        tempB = primeL[j]
        tempAL = [tempA[a1] for a1 in range(4)]
        tempBL = [tempB[b1] for b1 in range(4)]
        
        if tempAL[0] in tempBL and tempAL.count(tempAL[0])==tempBL.count(tempAL[0]) and \
           tempAL[1] in tempBL and tempAL.count(tempAL[1])==tempBL.count(tempAL[1]) and \
           tempAL[2] in tempBL and tempAL.count(tempAL[2])==tempBL.count(tempAL[2]) and \
           tempAL[3] in tempBL and tempAL.count(tempAL[3])==tempBL.count(tempAL[3]) :
            compareL.append(tempB)

    print compareL
    
    #step3 : diff calculate
    lenCompareL = len(compareL)
    if lenCompareL<=2 :
        pass
    else :
        for k1 in range(lenCompareL-1) :
            tempSrc = int(compareL[k1])
            for k2 in range(k1+1,lenCompareL) :
                tempSrc2 = int(compareL[k2])
                tempDiff = abs(tempSrc2-tempSrc)
                tempDestStr = str(tempSrc2 + tempDiff)

                if tempDestStr in compareL :                    
                    if not tempSrc==1487 :
                        print "Answer : ",compareL[k1],compareL[k2],tempDestStr,"diff : ",tempDiff
                        sys.exit()

#Answer :  2969 6299 9629 diff :  3330
