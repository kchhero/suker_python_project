maxNum = 0
for i in range(1,100) :
    for j in range(1,100) :
        tempStr = str(pow(i,j))
        localSum = 0
        for k in range(len(tempStr)) :
            localSum += int(tempStr[k])

        if localSum > maxNum :
            maxNum = localSum
            print "sum = ",maxNum, "value = ",tempStr, i,"^",j
