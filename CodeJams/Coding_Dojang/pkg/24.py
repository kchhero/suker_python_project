# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 13:58:01 2014

@author: choonghyun.jeon
"""
import re

problem = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
problemL = problem.split(',')

nameLee = str('이').encode('cp949')
nameKim = str('김').encode('cp949')
nameLeeJY = str('이재영').encode('cp949')

cnt_Lee = 0
cnt_Kim = 0
cnt_LeeJY = 0

finalList = []
        
for i in problemL : 
    temp = i.encode('cp949')
    if re.match(nameLee, temp) :  
        cnt_Lee += 1
    elif re.match(nameKim, temp) :  
        cnt_Kim += 1

    if re.match(nameLeeJY, temp) :  
        cnt_LeeJY += 1
        
    finalList.append(temp)

print "1. %s:%d, %s:%d"%(nameKim,cnt_Kim, nameLee,cnt_Lee)
print "2. %s : %d"%(nameLeeJY,cnt_LeeJY)
print "3. ",
for i in set(finalList) :
    print i,
print ""
print "4. ",finalList.sort()