# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 09:20:55 2014

@author: choonghyun.jeon
"""

print "initial data : "
problemS = raw_input()
tempL = problemS.split(' ')

N = int(tempL[0])
K = int(tempL[1])

soldiers = [i for i in range(1,N+1)]
compares = soldiers[:]

i = -1
removeL = []
soldiersNum = len(soldiers)
while soldiersNum > 1 :
    i += K
    if i >= soldiersNum :
        i = (-1)*(soldiersNum-(i-K))
        soldiers = compares[:]
        soldiersNum  = len(soldiers)
    else :
        compares.remove(soldiers[i])
        
print "answer : "
print soldiers
            