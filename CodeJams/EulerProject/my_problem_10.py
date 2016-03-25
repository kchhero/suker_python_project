# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:47:12 2014

@author: choonghyun.jeon
"""

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
        
    
t = 0

    
for j in xrange(1, 2000001,2) :
    if suker_isPrimeNum(j)==1:
        t += j
        
print "sum = ",t
print "ssum = %d"%t
