# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 09:07:16 2014

@author: choonghyun.jeon
"""

import math

problem = 600851475143

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

divNum = 2
while 1 :
    if problem%divNum == 0 :  # this is not a prime number
        problem /= divNum
        divNum = 2
    else :
        divNum += 1
    
    if divNum==problem :
        print "Answer : %d"%problem
        break