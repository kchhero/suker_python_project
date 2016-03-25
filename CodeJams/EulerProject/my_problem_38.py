maxPanD = 0

for num in range(1,50000) :    
    for k in range(1,10) :
        cnt = 0
        pandigital = []
        tempPanD = []
        for j in range(1,k+1) :
            temp=num*j            
            tempStr=str(temp)
            tempStrLen=len(tempStr)

            for i in range(tempStrLen) :
                if tempStr[i]=="0" :
                    i = tempStrLen
                elif tempStr[i] not in pandigital :
                    pandigital.append(tempStr[i])
                    cnt = cnt+1
                    tempPanD.append(tempStr[i])
                else :
                    tempPanD.append(tempStr[i])

        if cnt==9 and len(tempPanD)==9:
            if maxPanD < int("".join(pandigital)) :
                maxPanD = int("".join(pandigital))
                print "num is = ",num
                print "pandigital num = ",maxPanD
                print "n is = ",k
