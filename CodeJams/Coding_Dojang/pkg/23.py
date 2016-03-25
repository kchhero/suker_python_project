# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 13:47:26 2014

@author: choonghyun.jeon
"""

problemS = raw_input()
tempL = problemS.split(' ')
problemL = [int(i) for i in tempL]
maxCycle = 0

for i in range(problemL[0], problemL[1]+1) :
    num = i
    cycle = 1
    
    while num > 1 :
        if num%2==0 : #even
            num /= 2
        else :
            num = num*3 + 1
        cycle += 1
    
    if maxCycle < cycle :
        maxCycle = cycle
    
print problemL[0], problemL[1], maxCycle