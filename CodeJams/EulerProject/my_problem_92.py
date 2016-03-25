cnt = 0
saveCallStack1 = []
saveCallStack89 = []

for i in xrange(2,10000000) :
    tempStr = str(i)
    localSum = 0
    
    if i < 1000 :
        tempL = []
    while 1 :
        for j in range(len(tempStr)) :        
            tempInt = int(tempStr[j])
            localSum += tempInt**2
            
        if i < 1000 :
            tempL.append(localSum)
        
        if localSum==1 or localSum in saveCallStack1 :
            if i < 1000 :
                ttt = [k for k in tempL if not k in saveCallStack1]                
                saveCallStack1.extend(ttt)            
            break
        elif localSum==89 or localSum in saveCallStack89 :
            if i < 1000 :
                ttt = [k for k in tempL if not k in saveCallStack89]                
                saveCallStack89.extend(ttt)
            cnt += 1
            break
        else :
            tempStr = str(localSum)
            localSum = 0

    if i%100000==0 :
        print "going...", i
        
print saveCallStack1
print saveCallStack89
print "Answer : ",cnt

#8581146

