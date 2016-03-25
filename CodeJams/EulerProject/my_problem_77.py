import os
import math
import time

primeNums = []

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
        
def start() :
    global primeNums
    sukerPrimePath = os.getcwd() + "\\sukerPrimeList.txt"
    if os.path.isfile(sukerPrimePath) :
        primeNo = open(sukerPrimePath, 'r')
        primeNums = primeNo.readline().split(' ')
        #print len(primeNums)
        primeNo.close()

def mainn() :
    startTime = time.time()
    maxN = 10
    choiceCnt = maxN/2
    ll = primeNums[0:5]
    for i in range(choiceCnt,0,-1) :
        for j in range(choiceCnt) :
            for k in ll
        
    print "Done!!"
    print time.time() - startTime
    
if __name__ == "__main__" :
    start()
    mainn()