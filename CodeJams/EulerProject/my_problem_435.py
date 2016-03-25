fiboL = long([0]*(10**15))
sum = 0

def fibo(n) :
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

def init_fibo() :
    global fiboL
    fiboL = [fibo(i) for i in xrange((10**15)+1)]
    print "init_fibo Done"
    
def calculateF() :
    global sum    
    for x in range(101) :
        lSum = 0
        for j in xrange(1,(10**15)+1) :
            lSum = lSum + fiboL[j]*(x**j)
            sum += lSum
            
        print "x = ",x,"x sum = ",lSum," total sum = ",sum
    
init_fibo()
calculateF()
