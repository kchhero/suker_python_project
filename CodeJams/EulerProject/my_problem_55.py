def getReverseNum(n) :
    tempStr = str(n)
    tempL = [tempStr[i] for i in range(len(tempStr))]
    tempL.reverse()
    tempReverseStr = "".join(tempL)
    return int(tempReverseStr)

def checkPalindromeNum(n) :
    tempStr = str(n)
    for i in range(len(tempStr)/2) :
        if not tempStr[i]==tempStr[len(tempStr)-(i+1)] :
            return 0

    return 1

LychrelNumCnt = 0
for i in range(1,10001) :
    isNotLychrel=0
    temp = i
    for loopCnt in range(49) :
        reN = getReverseNum(temp)
        temp += reN
        if checkPalindromeNum(temp)==1 :#this is not lychrel number
            isNotLychrel=1
            break

    if isNotLychrel==0 :
        print "lychrel number : ",i
        LychrelNumCnt += 1

print "Lychrel Number Count : ",LychrelNumCnt
