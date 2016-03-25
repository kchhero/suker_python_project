# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 09:20:55 2014

@author: choonghyun.jeon
"""

arrayIn = raw_input()
problemL = arrayIn.split(' ') #input type : "1 6 10 4 7 9 5"

problemArray = [int(i) for i in problemL]
largestSubsetValue = 1
largestSubsetList = []
checkList = []

for i in problemArray :    
    cnt = 1
    tempList = [i]

    if i in checkList :
        pass
    else :
        orgNum = i
        
        #Right search    
        findNum = i
        while findNum+1 in problemArray :
            checkList.append(findNum+1)
            tempList.append(findNum+1)
            findNum += 1
            cnt +=1

        findNum = orgNum            
        #Left search
        while findNum-1 in problemArray :
            checkList.append(findNum-1)
            tempList.append(findNum-1)
            findNum -= 1
            cnt +=1        
        
        #Is largestSubset?
        if cnt > largestSubsetValue :
            largestSubsetValue = cnt
            largestSubsetList = tempList[:]

print "Largest Subset : ",largestSubsetList
            