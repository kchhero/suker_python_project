# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 09:47:56 2014

@author: choonghyun.jeon
어떤 값 n이 주어진다면 n/2 부터 역으로 가장큰 소수를 찾고 나누어 떨어지는지
확인해보면될듯.
"""

import math
import numpy

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

n = 600851475143

for i in xrange(numpy.int32(n/2+1),0,-1) :
    if suker_isPrimeNum(i)==1 :
        if n%i==0 :
            print "Big num is %d"%i
            break