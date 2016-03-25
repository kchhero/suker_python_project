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

def suker_factorization2L(n) :
    tempN = n
    tempFactoEle = 0
    sqrtNum = n/2
    _factoL = []

    if n<=2 :
        return _factoL
    elif n > 2 :        
        i = 2
        while i < sqrtNum and not tempN==1:
            if tempN%i==0 :
                if i in _factoL :
                    eleCnt = _factoL.count(i)
                    _factoL.remove(i)
                    eleCnt += 1
                    _factoL.append(i**eleCnt)
                else :
                    _factoL.append(i)
                tempN /= i
            else :
                i += 1

    return _factoL

def suker_factorial(n) :
    if n==2 :
        return 2
    elif n==1 :
        return 1
    else :
        return n*suker_factorial(n-1)

def suker_factorizationCnt(n,isNeedSum=0) :
    tempN = n
    tempFactoEle = 0
    sqrtNum = n/2#int(math.sqrt(n))
    _factoL = []#last is sum of factorizations elements
    finalSum = 1

    if n < 4 :
        print "digit number too small"

    else :    
        for i in range(2,sqrtNum+1) :
            if suker_isPrimeNum(i)==1 :
                while tempN%i==0 :
                    tempFactoEle += 1
                    tempN = tempN/i
                    #print "factoele = ",tempFactoEle
                    
                if not tempFactoEle==0 :
                    if isNeedSum==1 :
                        tempSum = 0
                        for s in range(tempFactoEle,0,-1) :                        
                            tempSum += pow(i,s)
                        tempSum += 1
                        
                        finalSum *= tempSum
                    
                    _factoL.append(tempFactoEle+1)
                    tempFactoEle = 0
                    
                if tempN==1 :
                    if isNeedSum==1 :
                        #print "finalSum = ",finalSum-n
                        _factoL.append(finalSum-n)
                    break
                
        if isNeedSum==1 :
            if len(_factoL)==0 :    #check prime
                if suker_isPrimeNum(n)==1 :
                    _factoL.append(1)
                    return _factoL

        return _factoL
                
def suker_getMaxGcd(a,b) :
    if a == b :
        return a
    elif a < b :
        return suker_getMaxGcd(b,a)
    else :
        temp = a-b
        if temp > 0 :
            return suker_getMaxGcd(a-b,b)
        elif temp < 0 :
            return suker_getMaxGcd(b,temp)
        else :
            return a
    
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

def suker_substr(str,start,stop) :
    return str[start:stop+1]
