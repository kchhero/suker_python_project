def _factorial(num) :
    if num==0 :
        return 1
    elif num==1 :
        return 1
    elif num==2 :
        return 2
    else :
        return num*_factorial(num-1)

def _initFactoList1To10(factoList) :
    for i in range(10) :
        factoList.append(_factorial(i))
    
sum = 0
facL = []

_initFactoList1To10(facL)
print facL

for i in range(3,9999999) :
    n = i
    localSum = 0
    while n >= 1 :
        temp = n%10
        n /= 10        
        localSum += facL[temp]
       # print localSum, facL[temp], n

    if localSum == i :
        print i
        sum += i

print "sum = ",sum
print "Done"
