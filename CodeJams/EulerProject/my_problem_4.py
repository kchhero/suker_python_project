# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:18:16 2014

@author: choonghyun.jeon
"""

maxNum = 0

for i in range(100,999) :
    for j in range(100,999) :
        temp = str(i*j)
        if len(temp)==5 :
            if temp[0]==temp[-1] and temp[1]==temp[-2] :                
                if maxNum < int(temp) :
                    maxNum = int(temp)
                #print(temp)
        elif len(temp)==6 :
            if temp[0]==temp[-1] and temp[1]==temp[-2] and temp[2]==temp[-3] :
                if maxNum < int(temp) :
                    maxNum = int(temp)
        else :
            pass

print("max number : ",maxNum)
        

"""
i = 952
j = 963
ss = str(i*j)
print(ss[0])
print(ss[1])
print(ss[2])
print(ss[-3])
print(ss[-2])
print(ss[-1])
"""
