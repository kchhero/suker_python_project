def _factorial(num) :
    if num==1 :
        return 1
    else :
        return num*_factorial(num-1)
        
facResult = str(_factorial(100))
facLen = len(facResult)
sum = 0

for i in range(facLen) :
    sum = sum + int(facResult[i])

print "sum = ", sum
