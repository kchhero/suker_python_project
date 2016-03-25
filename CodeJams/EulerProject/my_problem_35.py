def isPrime(n) :
    if n==2 or n==3 or n==5 :
        return 1
    else :
        if n%2==0 :
            return 0
        else :
            for i in range(3,n/3+3,2) :
                if n%i==0 :
                    return 0
                else :
                    pass
            return 1            

primeRotateL = []
primeRotateL.append(2)
for n in range(3,1000000,2) :
    needNotAppend = 0
    tempStr = str(n)
    for i in range(len(tempStr)) :
        if int(tempStr[i])%2==0 :
            needNotAppend = 1
            break

    if needNotAppend==0 :
        if isPrime(n) :
            primeRotateL.append(n)

print primeRotateL

cnt = 0
for p in primeRotateL :
    tempL = []
    tempStr = str(p)
    isGood = 1
    if len(tempStr)==1 :
        cnt += 1
    else :
        lenn = len(tempStr)
        for i in range(lenn) :
            tempL.append(tempStr[i])

        for i in range(lenn-1) :
            rotateStr = tempL.pop()
            tempL.insert(0,rotateStr)
            checkInt = int("".join(tempL))
            if checkInt in primeRotateL :
                pass
            else :
                isGood = 0
                break

        if isGood==1 :
            cnt += 1
            isGood = 0
            print checkInt

print "answer : ",cnt
