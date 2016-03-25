cnt = 1

for i in range(2,10) :
    for j in range(1,100) :
        temp = i**j
        tempStr = str(temp)
        if len(tempStr)==j :
            cnt += 1
            print i,"^",j,"=",temp
        elif len(tempStr) < j :
            break

print "Answer : ",cnt

#9 ^ 21 = 109418989131512359209
#Answer :  49
