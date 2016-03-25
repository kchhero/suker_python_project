# -*- coding: utf-8 -*-
"""
Created on Mon May 19 10:06:34 2014

@author: choonghyun.jeon
"""
import os
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

def start() :
    sukerPrimePath = os.getcwd() + "\\sukerPrimeList.txt"
    if os.path.isfile(sukerPrimePath) :
        primeNo = open(sukerPrimePath, 'r')
        primeNums = primeNo.readline().split(' ')
        lastNum = int(primeNums[-1])
        primeNo.close()
        
        newPrimeNo = open(sukerPrimePath, 'w')
        newPrimeNumsL = [i for i in range(lastNum+1,lastNum*10) if suker_isPrimeNum(i)==1]
        lll2 = [str(i) for i in newPrimeNumsL]
        lll3 = " ".join(primeNums)+' '+" ".join(lll2)        
        newPrimeNo.write(lll3)
        newPrimeNo.close()
        print "write until : " + str(newPrimeNumsL[-1]) + " Done!"
        
    else :
        primeNo = open(sukerPrimePath, 'w')
        primeL = [i for i in range(3,100) if suker_isPrimeNum(i)==1]
        lll = [str(i) for i in primeL]
        primeNo.write(" ".join(lll))        
        primeNo.close()
        
if __name__ == "__main__" :
    start()
