import math
import sys

def suker_isPrimeNum(n) :
    if n==2 or n==3 or n==5 or n==7 :
        return 1
    elif n%2==0 :
        return 0
    else :
        sqrtNum = int(math.sqrt(n))
        for i in range(3,sqrtNum+1) :
            if n%i==0 :
                return 0

        return 1

for i in xrange(987654321, 1, -9) :
    isSkip=0
    if i%2==0 or i%5==0 :
        pass
    else :
        d = []
        tempStr = str(i)
        tempStrLen = len(tempStr)
        d = [tempStr[j] for j in range(tempStrLen)]

        if '0' in tempStr :
            isSkip = 1
        else :
            if tempStrLen<9 :
                for jj in range(tempStrLen) :
                    if int(tempStr[jj]) > tempStrLen :
                        isSkip=1
                        break

        if isSkip==0 :
            if len(tempStr)==len(set(tempStr)) :
                print i
                if suker_isPrimeNum(i)==1 :
                    print "Answer = ",i
                    sys.exit()

#answer=7652413
