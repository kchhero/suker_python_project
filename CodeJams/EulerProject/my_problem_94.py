import math

def triNN(a=1,b=1,c=1) :
    """
    s1 = a+b+c
    if not s1%2==0 :
        return 0
    elif not c%2==0 :
        return 0
    else :
        return c*math.sqrt(b*b-(c*c)/4)/2
    """
    s1 = a+b+c
    if not s1%2==0 :
        return 0
    else :
        s2 = s1/2
        return math.sqrt(s2*(s2-a)*(s2-b)*(s2-c))

def getH2(a=1,b=1,c=1) :
    return math.sqrt(a*a-(c*c)/4)

sum = 0
nN = 0
#for a in xrange(3,300000001) :
for a in xrange(20000000,30000001) :
    for i in range(2) :
        if i==0 :
            c = a-1
        else :
            c = a+1
                      
        h2 = float(getH2(a,a,c))/2
        sS = float(c*h2)
        if sS==int(sS) and not sS==0:
            nN = a*2+c            
            sum += nN
            #print "===>",nN,a,a,c
            
    if a%10000000==0 :
        print "a is pass",a, nN
        
print "Answer = ",sum

#          3 ~ 333,333,334 : 312,530,549,665,725,889

#          3 ~  10,000,001 :       1,078,145,912,809
# 10,000,000 ~  20,000,001 :      16,150,072,412,336
# 20,000,000 ~  30,000,001 :      70,337,636,689,862
#330,000,000 ~ 333,333,335 :   6,633,336,656,666,670



