import math

def suker_factorial(n) :
    if n==2 :
        return 2
    elif n==1 :
        return 1
    else :
        return n*suker_factorial(n-1)

def suker_factorization(n,isNeedSum) :
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

tempL = []
for i in range(6,10001,1) :
    if suker_isPrimeNum(i)==0 :
        temp = suker_factorization(i,1)#'220
        temp2 = temp.pop()#'284
        
        temp3 = suker_factorization(temp2,1)#'284
        temp4 = temp3.pop()#'220

        if i==temp4 and not i==temp2:
            print i,temp2
            tempL.append(i)
            tempL.append(temp2)

sum = 0
tttL = set(tempL)
print tttL

for i in tttL :
    sum += int(i)

print "sum = ",sum



