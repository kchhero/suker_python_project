# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 09:20:55 2014

@author: choonghyun.jeon
"""

arrayIn = raw_input()
problemL = arrayIn.split(' ') #input type : "1 3 4 8 13 17 20"
problemArray = [int(i) for i in problemL]
minDiff = problemArray[-1]-problemArray[0]
answerL = []

while len(problemArray) > 1 :
    checkNum = problemArray.pop(0)    
    diff = 1    
    while 1 :
        if checkNum+diff in problemArray :        
            if diff < minDiff :
                minDiff = diff
                answerL = [checkNum,diff]
            break
        else :
            diff += 1
        
print "Answer : {%d,%d}"%(answerL[0],(answerL[0]+answerL[1]))
            