col = 20
row = 20
wayCnt = 0

def _factorial(n) :
    if n==1 :
        return 1
    elif n==2 :
        return 2
    else :
        return n*_factorial(n-1)

wayCnt = _factorial(col*2)/(_factorial(col)*_factorial(row))

print "wayCnt = ",wayCnt
            
