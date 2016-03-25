# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 16:08:34 2014

@author: choonghyun.jeon
"""

leftV = 1.0
rightV = 0.0

for i in range(2,46) :
    if i != 5 :
        leftV *= (float)(i*i)
    
for j in range(2,46) :
    if j != 5 :
        rightV += (float)(leftV/(j*j))
    
    
print leftV/2
print rightV
    