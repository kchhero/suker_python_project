def suker_getMaxGcd(a,b) :
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

def checkPermutation(a,b) :
    aStr = str(int(a))
    bStr = str(int(b))
    aL = [aStr[i] for i in range(len(aStr))]
    bL = [bStr[i] for i in range(len(bStr))]
    aL.sort()
    bL.sort()
    aStr = "".join(aL)
    bStr = "".join(bL)
    if aStr==bStr :
        return 1
    else :
        return 0
    print aL,aStr
    print bL,bStr
    print ""
    
minValue = 100.0
minN = 0
for n in range(2,10000000) :
    phi = 0
    for i in range(1,n) :
        if suker_getMaxGcd(n,i)==1 :
            phi += 1.0
            
    temp = n/phi
    if minValue > temp :
        #phi is permutation number of n
        if checkPermutation(phi,n)==1 :
            print "min n : ",n, "n/phi : ",n,phi
            minValue = temp
            minN = n
            print ""
    
print "final : ",minN

print 87109/79180.0
