bigLargeNum = pow(2,1000)
bigLargeNumStr = str(bigLargeNum)

#print bigLargeNum
lenNum = len(bigLargeNumStr)
sum = 0

for i in range(lenNum) :
    sum = sum + int(bigLargeNumStr[i])

print "total sum = ",sum
    
