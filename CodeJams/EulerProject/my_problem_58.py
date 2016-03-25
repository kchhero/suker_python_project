# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:55:48 2015

@author: choonghyun.jeon
"""

import math
import time

def isPrime(n) :
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

def problem58() :        
    cornerL = []
    n = 1
    acc = 2
    primeCrossNum = 0    
    totalCrossNum = 1
    length0 = 1
    
    ttt = time.time()
    for squareNum in range(1,60000) :
        if squareNum==1 :
            cornerL.append(n)
        else :
            for i in range(4) :
                n += acc
                cornerL.append(n)
                if isPrime(n)==1 :
                    primeCrossNum += 1    
    
            acc += 2    
            totalCrossNum += 4
        
        print primeCrossNum,"/",totalCrossNum, "squareNum : ",squareNum
        if 100*primeCrossNum/totalCrossNum < 10 and not squareNum==1:
            print "answer : ",length0
            break
        
        length0 += 2
        
    print "time%f"%(time.time()-ttt)

if __name__ == "__main__":
    try : 
        #profile.run('main()')
        problem58()
    finally : 
        pass