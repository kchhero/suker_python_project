def suker_factorial(n) :
    if n==2 :
        return 2
    elif n==1 or n==0 :
        return 1
    else :
        return n*suker_factorial(n-1)

cnt = 0
tempL = []
for n in range(1,101) :
    for r in range(n+1) :
        valueC = suker_factorial(n)/(suker_factorial(r)*suker_factorial(n-r))
        if valueC >= 1000000 :            
            print n,"C",r,"=",valueC
            cnt += 1
            #if not valueC in tempL :
            #    tempL.append(valueC)

#print "count = ",len(tempL)
print "count = ", cnt
