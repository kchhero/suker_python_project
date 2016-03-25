import os
import math
import time

primeNumsOrg = []

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
    global primeNumsOrg
    sukerPrimePath = os.getcwd() + "\\sukerPrimeList_high.txt"
    if os.path.isfile(sukerPrimePath) :
        primeNo = open(sukerPrimePath, 'r')
        primeNumsOrg = primeNo.readline().split(' ')
        #print len(primeNums)
        primeNo.close()

def mainn() :
    global primeNumsOrg
    tempPrimeL = primeNumsOrg[:]
    lengg = len(tempPrimeL[-1])/2 + 1
    savingL_2 = []
    savingL_3 = []

    i1 = tempPrimeL.pop(0)
    while len(tempPrimeL)>0 :
        i1 = tempPrimeL.pop(0)
        if len(i1) >= lengg :
            break
        
        for i2 in tempPrimeL :
            stt1 = i1+i2
            if stt1 in primeNumsOrg :
                stt2 = i2+i1
                if stt2 in primeNumsOrg :
                    savingL_2.append(i1)
                    savingL_2.append(i2)
                

    print "step1 : done : "
    savingL_2 = list(set(savingL_2[:]))
    print savingL_2
    
#    savingL_2 = ['43', '61', '89', '67', '83', '23', '47', '29', '41', '3', '97', '7', '719', '73', '71', '79', '11', '13', '59', '17', '19', '31', '37', '53']
    tempPrimeL1 = savingL_2[:]
    tempPrimeL2 = savingL_2[:]
    cnt = 0
    
    while len(tempPrimeL1)>0 :
        cnt = 0
        i1 = tempPrimeL1.pop(0)
        for i2 in tempPrimeL2 :
            if i1 == i2 :
                pass
            else :
                stt1 = i1+i2
                if stt1 in primeNumsOrg :
                    stt2 = i2+i1
                    if stt2 in primeNumsOrg :
                        cnt += 1
        
        if cnt >= 4 :
            savingL_3.append(i1)

    print "step2 : done : "
    savingL_3 = list(set(savingL_3[:]))
    print savingL_3

    
if __name__ == "__main__" :
    start()
    mainn()
    
#1. find pair 2 numbers
#2. by 1. found, 3 select in list, again 3 paires
#3. repeate