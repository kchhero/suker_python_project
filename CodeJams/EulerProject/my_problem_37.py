import math

def suker_isPrimeNum(n) :
    if n==2 or n==3 or n==5 or n==7 :
        return 1
    elif n%2==0 :
        return 0
    else :
        sqrtNum = int(math.sqrt(n))
        for i in range(3,sqrtNum+1) :
            if n%i==0 :
                return 0

        return 1

sum = 0
cnt = 0
for i in range(13,1000000,2) :
#for i in range(13,333,2) :
    if suker_isPrimeNum(i)==1 :
        tempStr = str(i)
        checkL = [tempStr[j] for j in range(len(tempStr))]
        nonPropertyNum=0
        
        #right remove check
        tempL = checkL[:]
        for k in range(len(tempStr)-1) :            
            tempL.pop()
            checkNum = int("".join(tempL))
            if checkNum==1 :
                nonPropertyNum=1
                break
            elif suker_isPrimeNum(checkNum)==0 :
                nonPropertyNum=1
                break

        if nonPropertyNum==0 :
            #left remove check
            tempL = checkL[:]
            for k in range(len(tempStr)-1) :                
                tempL.pop(0)
                checkNum = int("".join(tempL))
                if checkNum==1 :
                    nonPropertyNum=1
                    break
                elif suker_isPrimeNum(checkNum)==0 :
                    nonPropertyNum=1
                    break
                
            if nonPropertyNum==0 :
                cnt += 1
                sum += i
                print i, cnt
                if cnt==11 :
                    break

print "sum = ",sum,cnt
        
