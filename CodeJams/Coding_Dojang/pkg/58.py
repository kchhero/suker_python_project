# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:10:42 2014

@author: choonghyun.jeon
"""

#한개의 문자를 삽입,제거,변환을 했을 경우라고 가정했으므로
#글자수가 같으면 변환에 대한 검증
#글자수가 다르면 삽입 또는 제거로 판별

def OneEditApart(s1,s2) :
    diffCnt = 0
    s1Len = len(s1)
    s2Len = len(s2)

    if s1Len==s2Len :
       for i in range(s1Len) :
           if s1[i] != s2[i] :
               diffCnt += 1
       if diffCnt <= 1 :
            return True
    else :
        if abs(s1Len-s2Len) == 1 :            
            (bigText,smallText) = (s1,s2) if s1Len > s2Len else (s2,s1)
            sL = list(bigText)
            for i in range(len(bigText)) :
                tempL = sL[:]
                tempL.pop(i)                    
                if "".join(tempL)==smallText :
                    return True
    return False

print OneEditApart("cat", "dog")
print OneEditApart("cat", "cats")
print OneEditApart("cat", "cut")
print OneEditApart("cat", "cast")
print OneEditApart("cat", "at")
print OneEditApart("cat", "acts")

print OneEditApart("cat", "cats's")
print OneEditApart("cat", "catwoman")
print OneEditApart("cat", "ccatt")
print OneEditApart("cat", "ct")

print OneEditApart("suker", "suer")
print OneEditApart("suker", "suker's")
print OneEditApart("suker", "sukers")