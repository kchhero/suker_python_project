# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 09:32:38 2014

@author: choonghyun.jeon
"""

n1 = 1
n2 = 2
t = 0
LL = [n1,n2]

while t <= 4000000 :
    t = n1+n2
    LL.append(t)
    n1 = n2
    n2 = t    

sum = 0    
for i in LL :
    if i%2==0 :
        sum += i

print sum