d = []
cnt = 0

d.append(0)
for i in range(1,1000001) :
    tempStr = str(i)
    tempStrLen = len(tempStr)
    for j in range(tempStrLen) :
        d.append(tempStr[j])
                
    cnt += tempStrLen
    if cnt > 1000000 :
        break

print d[1]
print d[10]
print d[100]
print d[1000]
print d[10000]
print d[100000]
print d[1000000]

print "mul = ",int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])
