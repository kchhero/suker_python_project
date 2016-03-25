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

maxNum = 50000000
#maxNum = 50
primeL = []
primeL.append(2)

for n in xrange(3,maxNum,2) :    
    if suker_isPrimeNum(n)==1 :
        primeL.append(n)
        if n**2 >= maxNum :
            break

cnt = 0

#50000000 ## 1/4 = 84.x,  85
#50000000 ## 1/3 = 368.x, 369
#50000000 ## 1/2 = 7071.x 7072

prime1L = [i for i in primeL if i < 7074]
prime2L = [i for i in primeL if i < 370]
prime3L = [i for i in primeL if i < 87]
#prime1L.reverse()
#prime2L.reverse()
#prime3L.reverse()

#print prime1L,len(prime1L)
#print prime2L,len(prime2L)
#print prime3L,len(prime3L)

for c in prime3L :
    for b in prime2L :
        #sizePrime1L = len(prime1L)
        for a in prime1L :
            s = a**2+b**3+c**4
            if s < maxNum :
                cnt += 1#sizePrime1L
               # print "cnt = ",cnt,sizePrime1L,a,b,c                
                #break
            
            #sizePrime1L -= 1
print "finalCnt = ",cnt
