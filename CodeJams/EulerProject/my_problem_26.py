def isPrimeNum(n) :
    if n%2==0 :
        return 0
    elif n==2 or n==3 :
        return 1
    else :
        for i in range(3,n/3+3,2) :
            if n%i==0 :
                return 0

        return 1

orgL = [i for i in range(3,1001)]
pL = []

for p in orgL :
    temp = p
    while temp%2==0 or temp%5==0 :
        if temp%2==0 :
            temp /= 2 
        elif temp%5==0 :
            temp /= 5

    pL.append(temp)
        
pL = set(pL)
pL.remove(1)
print pL

maxNum = -1
for pp in pL :
    tempStrL = []
    for i in range(1,1000) :
        tempStrL.append("9")
        tempI = int("".join(tempStrL))
        if tempI%pp == 0 :
            if maxNum < i :
                maxNum=i
                print "update MaxNum = ",maxNum, pp
            break

print "maxNum = ",maxNum
    
        
    
