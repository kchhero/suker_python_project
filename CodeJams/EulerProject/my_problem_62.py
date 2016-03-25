start = 600
end = 60000
isFinish=0

while isFinish==0 :
    baseNumStr = str(pow(start,3))
    baseNumCnt = len(baseNumStr)
    tempL = []
    orgLL = []
    print "baseNumStr :",baseNumStr,start,end
    for n in range(start,end) :
        tempStr = str(pow(n,3))
        if len(tempStr)==baseNumCnt :
            temp2L = list(tempStr)
            orgLL.append(n)
            temp2L.sort()
            tempL.append("".join(temp2L))
        else :
            print "start :",start,"end :",n
            start = n
            #print "start :",start,n,pow(n,3)
            #isFinish=1
            break
        
    if not start==n :
        isFinish=1
        
    for kk in range(len(tempL)) :
        cnt = 0
        cccL = []
        cccL.append(kk)
        tt = tempL[kk]
        for kk2 in range(kk+1,len(tempL)) :
            if tt==tempL[kk2] :
                cccL.append(kk2)
                cnt += 1

        if cnt >= 4 :
            print "OOO ==>",kk,orgLL[kk],cccL
            print "PPP ==>",
            for i in cccL :
                print orgLL[i],
            isFinish=1
            print "Answer = ",pow(orgLL[cccL[0]],3)
            break

#127035954683
