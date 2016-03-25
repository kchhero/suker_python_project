import math

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

#41 = 2 + 3 + 5 + 7 + 11 + 13
primeL = [i for i in xrange(3,1000001,2) if suker_isPrimeNum(i)==1]
print "prime make done!"

maxLength = 0
for i in range(len(primeL)) :
    cnt = 0
    sum = 0
    for j in range(i,len(primeL)) :
        sum += primeL[j]
        cnt += 1
        if sum in primeL and cnt > maxLength :
            maxLength = cnt
            print "start Num :",primeL[i], "end Num :",primeL[j], "max Length :",maxLength, "sum :",sum

#start Num : 7 end Num : 3931 max Length : 543 sum : 997651
            
