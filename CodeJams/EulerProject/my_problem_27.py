def isPrimeNum(n) :
    if n%2==0 :
        return 0
    elif n==2 or n==3 :
        return 1
    else :
        for i in range(3,n/3+3,2) :
            if n%i==0 :
                return 0

        return 1
    
def shit(a,b) :
    cnt = 0
    for n in range(100) :
        checkNum = pow(n,2)+(a*n)+b

        if checkNum > 0 :
            if isPrimeNum(checkNum) :
                cnt = cnt + 1
            else :
                return cnt

maxCnt = 0
for a in range(-999,1001,1) :
    for b in range(-999,1001,1) :
        cnt = shit(a,b)
        if maxCnt < cnt :            
            maxCnt = cnt
            properA = a
            properB = b
            print "a = ",a, " b = ",b
            print "prime count = ",maxCnt
            print "answer = ",a*b


