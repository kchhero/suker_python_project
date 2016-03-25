import math

def suker_factorization(n) :
    tempN = n
    tempFactoEle = 0
    sqrtNum = n/2#int(math.sqrt(n))
    _factoL = []
    
    for i in range(2,sqrtNum+1) :
        if suker_isPrimeNum(i)==1 :
            while tempN%i==0 :
                tempFactoEle += 1
                tempN = tempN/i

            if not tempFactoEle==0 :
                _factoL.append(tempFactoEle+1)
                tempFactoEle = 0
                
            if tempN==1 :
                break

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

maxNum = 0
triDigitNum = 0
for i in range(1,100000) :
    triDigitNum += i
    tempNum = 1
    if triDigitNum>1000 :
        for j in suker_factorization(triDigitNum) :
            tempNum *= j

        if maxNum < tempNum :
            maxNum = tempNum
            if maxNum >=500 :
                print "tri Num : ",triDigitNum," step : ",i, "cnt : ",maxNum
                break
                
            print "tri Num : ",triDigitNum," step : ",i, "cnt : ",maxNum

"""
tri Num :  1035  step :  45 cnt :  12
tri Num :  1128  step :  47 cnt :  16
tri Num :  1176  step :  48 cnt :  24
tri Num :  2016  step :  63 cnt :  36
tri Num :  3240  step :  80 cnt :  40
tri Num :  5460  step :  104 cnt :  48
tri Num :  25200  step :  224 cnt :  90
tri Num :  73920  step :  384 cnt :  112
tri Num :  157080  step :  560 cnt :  128
tri Num :  437580  step :  935 cnt :  144
tri Num :  749700  step :  1224 cnt :  162
tri Num :  1385280  step :  1664 cnt :  168
tri Num :  1493856  step :  1728 cnt :  192
tri Num :  2031120  step :  2015 cnt :  240
tri Num :  2162160  step :  2079 cnt :  320
tri Num :  17907120  step :  5984 cnt :  480
tri Num :  76576500  step :  12375 cnt :  576
"""
