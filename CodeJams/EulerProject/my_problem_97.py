n = 1
eventStep=1

targetNum = 7830457
namuge = 0
while 1 :
    if eventStep==1 :
        temp = 2**n
        tempStr = str(temp)
        
        if len(tempStr)<11 :
            n += 1
        else :
            baseStepNum = n
            eventStep=2
    elif eventStep==2 :
        temp = 2**baseStepNum
        tempStr = str(temp)
        tempStr11 = tempStr[len(tempStr)-11:]
        print "step : n = ",n," 11 digit :",temp
        eventStep=3
        temp = int(tempStr11)
    elif eventStep==3 :
        baseStepNum *= 2
        if baseStepNum <= targetNum :
            temp = temp**2
            tempStr = str(temp)
            tempStr11 = tempStr[len(tempStr)-11:]        
            temp = int(tempStr11)
        else :            
            namuge = targetNum - (baseStepNum/2)
            print namuge,temp,targetNum
            if namuge > 30 :
                targetNum = namuge
                baseStepNum = n
            else :
                namuge += (baseStepNum/2)                
                print namuge,temp,2**n
                break

print "Answer =",28433*(2**namuge)*temp+1
