upperNum = 3
belowNum = 2
cnt = 0

for i in range(1000-1) :
    print upperNum,"/",belowNum
    oldUpperNum = upperNum
    upperNum = upperNum+belowNum*2
    belowNum = oldUpperNum+belowNum

    tempUStr = str(upperNum)
    tempBStr = str(belowNum)
    if len(tempUStr) > len(tempBStr) :
        cnt += 1

print "Answer = ",cnt
    
    
