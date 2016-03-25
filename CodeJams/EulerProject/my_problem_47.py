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
    
def suker_factorization2L(n) :
    tempN = n
    tempFactoEle = 0
    sqrtNum = n/2+1
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

temp1L = []
temp2L = []
temp3L = []
temp4L = []
#for i in range(100000,1000000) :
i = 10
while i < 650000 :
    i += 1
    if suker_isPrimeNum(i)==1 :
        pass
    elif suker_isPrimeNum(i+1)==1 :
        i += 1
        pass
    elif suker_isPrimeNum(i+2)==1 :
        i += 2
        pass
    elif suker_isPrimeNum(i+3)==1 :
        i += 3
        pass
    else :
        if len(temp1L)==0 :
            temp1L = suker_factorization2L(i)
            temp2L = suker_factorization2L(i+1)
            temp3L = suker_factorization2L(i+2)
            temp4L = suker_factorization2L(i+3)
        else :
            temp1L = temp2L
            temp2L = temp3L
            temp3L = temp4L
            temp4L = suker_factorization2L(i+3)

            if not len(temp1L) == 4 :
                pass
            elif not len(temp2L) == 4 :
                i += 1
                pass
            elif not len(temp3L) == 4 :
                i += 2
                pass            
            elif not len(temp4L) == 4 :
                i += 3
                pass 
            else :
                if len(temp1L) == 4 and len(temp2L) == 4 and \
                   len(temp3L) == 4 and len(temp4L) == 4 :
                    tempSumL = temp1L + temp2L + temp3L + temp4L
                    if len(tempSumL)==len(set(tempSumL)) :
                        print "Answer : ",i, i+1, i+2, i+3
                        print tempSumL
                        print set(tempSumL)
                        break
                
print "Done!"
"""
Answer :  134043 134044 134045 134046
[3, 7, 13, 491, 4, 23, 31, 47, 5, 17, 19, 83, 2, 9, 11, 677]
set([83, 3, 4, 5, 7, 9, 491, 13, 47, 11, 17, 19, 677, 23, 2, 31])

"""
