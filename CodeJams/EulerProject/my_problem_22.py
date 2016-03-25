lineL = []

#array save
try :
    with open("my_problem_22_name.txt") as data :
        for line in data :
            lineL = line.split(',')
            
except IOError :
    print "File open error"

lineL.sort()

totalSum = 0
limit = len(lineL)
for i in range(limit) :
    tempStr = lineL[i]
    tempStrLen = len(tempStr)
    sum = 0
    for j in range(tempStrLen) :
        sum += ord(tempStr[j])-64
        
    totalSum += (i+1)*sum

print "Total Sum = ", totalSum
