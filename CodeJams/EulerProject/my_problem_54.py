"""
High Card : 1
One Pair : 2
Two Pairs : 3
Three of a Kind : 4
Straight : 5
Flush : 6
Full House : 7
Four of a Kind : 8
Straight Flush : 9
Royal Flush : 10
"""
import sys

def getPoint(pL) :
    numL = []
    numL = [i[0] for i in pL]
    shapeL = [i[1] for i in pL]    
    sortedNumL = sorted(numL)
    tempJoinedNumStr = "".join(sortedNumL)
    
    #Royal Flush
    if "AJKQT"==tempJoinedNumStr and len(set(shapeL))==1 :
        print "RoyalFlush : ", pL
        sys.exit()
        return 1000
    #Straight Flush
    elif "12345"==tempJoinedNumStr or "23456"==tempJoinedNumStr or "34567"==tempJoinedNumStr or \
         "45678"==tempJoinedNumStr or "56789"==tempJoinedNumStr or "6789T"==tempJoinedNumStr or \
         "789JT"==tempJoinedNumStr or "89JQT"==tempJoinedNumStr or "9JKQT"==tempJoinedNumStr :
        subPoint = 0
        if tempJoinedNumStr[4]=='A' :
            subPoint = 14
        elif tempJoinedNumStr[4]=='K' :
            subPoint = 13
        elif tempJoinedNumStr[4]=='Q' :
            subPoint = 12
        elif tempJoinedNumStr[4]=='J' :
            subPoint = 11
        elif tempJoinedNumStr[4]=='T' :
            subPoint = 10
        else :
            subPoint = int(tempJoinedNumStr[4])
            
        if len(set(shapeL))==1 :
            print "Straight Flush ", pL, 900+subPoint
            sys.exit()
            return 900+subPoint
        else :
            print "Straight ",pL, 900+subPoint
            return 500+subPoint
    elif len(set(numL))==2 :
        lTemp = numL[0]
        cnt = 0
        for ll in numL :
            if lTemp==ll :
                cnt += 1
        if cnt==2 or cnt==3 :
            print "Full House",pL
            return 700
        else :            
            print "Four card", pL
            sys.exit()
            return 800
    elif len(set(shapeL))==1 :
        print "Flush : ", pL        
        return 600
    elif len(set(numL))==3 :
        ntemp1 = sortedNumL[0]
        ntemp2 = sortedNumL[1]
        ntemp3 = sortedNumL[2]
        ntemp4 = sortedNumL[3]
        if sortedNumL.count(ntemp1)==3 or sortedNumL.count(ntemp2)==3 or sortedNumL.count(ntemp3)==3 :
            if sortedNumL.count(ntemp1)==3 :
                tempStrr = ntemp1
            elif sortedNumL.count(ntemp2)==3 :
                tempStrr = ntemp2
            else :
                tempStrr = ntemp3
            
            subPoint = 0
            if tempStrr=='A' :
                subPoint = 14
            elif tempStrr=='K' :
                subPoint = 13
            elif tempStrr=='Q' :
                subPoint = 12
            elif tempStrr=='J' :
                subPoint = 11
            elif tempStrr=='T' :
                subPoint = 10
            else :
                subPoint = int(tempStrr)
                
            #print "Three Pairs : ", pL, 400+subPoint            
            return 400+subPoint
        else :
            templlL = []
            subPoint = 0
            if sortedNumL.count(ntemp1)==2 and not ntemp1 in templlL :
                templlL.append(ntemp1)
            if sortedNumL.count(ntemp2)==2 and not ntemp2 in templlL :
                templlL.append(ntemp2)
            if sortedNumL.count(ntemp3)==2 and not ntemp3 in templlL :                
                templlL.append(ntemp3)
            if sortedNumL.count(ntemp4)==2 and not ntemp4 in templlL :
                templlL.append(ntemp4)

            if 'A' in templlL :
                subPoint = 14
            elif 'K' in templlL :
                subPoint = 13
            elif 'Q' in templlL :
                subPoint = 12
            elif 'J' in templlL :
                subPoint = 11
            elif 'T' in templlL :
                subPoint = 10
            else :
                templlL.sort()
                subPoint = int(templlL[1])                
           
            print "Two Pairs : ", pL, 300+subPoint
            return 300+subPoint
    elif len(set(numL))==4 :
        for i in numL :
            if numL.count(i)==2 :
                subPoint = 0
                if i=='A' :
                    subPoint = 14
                elif i=='K' :
                    subPoint = 13
                elif i=='Q' :
                    subPoint = 12
                elif i=='J' :
                    subPoint = 11
                elif i=='T' :
                    subPoint = 10
                else :
                    subPoint = int(i)
                    
                #print "One Pair : "+i, pL, 200+subPoint                
                return 200+subPoint
    else :
        if 'A' in numL :
            subPoint = 14
        elif 'K' in numL :
            subPoint = 13
        elif 'Q' in numL :
            subPoint = 12
        elif 'J' in numL :
            subPoint = 11
        elif 'T' in numL :
            subPoint = 10
        else :
            subPoint = int(sortedNumL[4])           
        
        #print "High Card : ", pL,100+subPoint
        return 100+subPoint


player1 = []
player2 = []
p1WinCnt = 0
p2WinCnt = 0
try :
    with open("my_problem_54_text.txt") as data :
        for line in data :
            tempL = line.strip().split(' ')
            player1.append(tempL[0:5])
            player2.append(tempL[5:10])

except IOError :
    print "File open error"


for i in range(len(player1)) :
    p1Point = getPoint(player1[i])
    p2Point = getPoint(player2[i])

    if p1Point > p2Point :
        p1WinCnt += 1
    elif p1Point==p2Point :
        p2WinCnt += 1
        print player1[i],player2[i]
    else :
        p2WinCnt += 1
        print "Player2 win"
        #break

print "Answer Player1 win count : ",p1WinCnt,p2WinCnt
