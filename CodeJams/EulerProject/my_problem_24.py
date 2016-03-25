def suker_factorial(n) :
    if n==2 :
        return 2
    elif n==1 :
        return 1
    else :
        return n*suker_factorial(n-1)

kk = [i for i in range(10)]

def checkBaseNum(n,base) :
    i = 1
    temp = n
    while temp <= base :
        i += 1
        temp = n*i

    return i-1

answer = []
baseNum = 1000000
for n in range(9,1,-1) :
    temp = checkBaseNum(suker_factorial(n),baseNum)
    if not temp == 0 :
        print baseNum,"-",suker_factorial(n)*temp
        baseNum -= suker_factorial(n)*temp

    print "count = ",temp
    aNum = kk[temp]
    print "n jari num : ",aNum, "facorial num : ",n,suker_factorial(n)
    answer.append(aNum)
    kk.remove(aNum)
    print kk,"\n"

for i in kk :
    answer.append(i)
    
print answer
#2783915604
#real answer is 1 step before
# so below is real answer
#2783915460
