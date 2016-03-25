import math

def fiveNums(n) :
    return n*(3*n-1)/2

fiveNumL = [fiveNums(i) for i in range(1,10000)]

minn = 99999999
for i in range(len(fiveNumL)-1) :
    limit = i+1200
    if limit > len(fiveNumL) :
        limit = len(fiveNumL)
        
    for j in range(i+1,limit) :
        plus = fiveNumL[i]+fiveNumL[j]
        minus = abs(fiveNumL[j]-fiveNumL[i])

        if plus in fiveNumL and minus in fiveNumL :
            print "correct : ",fiveNumL[i],fiveNumL[j],i,j
            if minn > minus :
                minn = minus
                print "Update minus value :",minus

print ""
print "Answer : ",minn

#correct :  1560090 7042750 1019 2166
#answer : 5482660
