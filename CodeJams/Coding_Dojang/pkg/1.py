# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 14:13:39 2014

@author: choonghyun.jeon
"""

selfNum = [i for i in range(5001)]

for i in range(1, 5001) :
    sum = i
    temp = list(str(i))
    for j in temp :
        sum += int(j)
    
    if sum in selfNum :
        selfNum.remove(sum)
        
answer = 0
for i in selfNum :
    answer += i
    
print answer
    