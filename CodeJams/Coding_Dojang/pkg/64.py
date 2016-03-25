# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 16:17:31 2014

@author: choonghyun.jeon
"""

import time

timeCheck = time.time()

pp = [0]*1001

for a in range(1,1000) :
    for b in range(a,1000) :
        for c in range(b,1000) :
            _sum = a+b+c
            if _sum <= 1000 :
                if (c*c)==(a*a+b*b) :
                    temp = pp[_sum]
                    pp[_sum] = temp+1
                    print "a,b,c = ",a,b,c
                    print "pp and sum",pp[a+b+c], a+b+c
            else :
                break
            
temp = max(pp)
for i in range(1001) :
    if temp==pp[i] :
        print i,temp

            
print time.time()-timeCheck