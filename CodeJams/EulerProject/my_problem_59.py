import sys

text = []
convertText = []

#array save
try :
    with open("my_problem_59_cipher1.txt") as data :
        for line in data :
            text = line.strip().split(',')
except IOError :
    print "File open error"

convertTextInt = [int(dd) for dd in text]
lenConvertText = len(convertText)

convertRangeStart = 97
convertRangeEnd = 122

keySuspects = []
maxChr = ' '

for t1 in range(convertRangeStart,convertRangeEnd+1) :
    for t2 in range(convertRangeStart,convertRangeEnd+1) :
        for t3 in range(convertRangeStart,convertRangeEnd+1) :
            kk = [t1,t2,t3]
            tempConvertedText = []
            tempPreCheck = convertTextInt[0]
            
            temp = chr(kk[0]^tempPreCheck)            
            if temp=='.' or temp=='-' or temp==',' or temp=='+' or temp=='*' \
               or temp==')' or temp=='}' or temp=='{' or temp=='0' \
               or temp=='$' or temp=='`' or temp=='\'' or temp=='&' or temp=='%' \
               or temp=='#' or temp=='\"' or temp=='!' or temp==' ' \
               or temp=='?' or temp=='>' or temp=='=' or temp=='<' or temp==';' \
               or temp==':' or (ord(temp)>=49 and ord(temp)<=57) or temp=='/' \
               or ord(temp)>126 or temp=='~': 
                pass
            else :
                ttt = 0
                for src in convertTextInt :
                    temp = kk[ttt]^src
                    tempConvertedText.append(chr(temp))
                    ttt +=1 
                    if ttt==3 :
                        ttt = 0
                
                tempConvertedTextStr = "".join(tempConvertedText)
                if "The" in tempConvertedTextStr :
                    print tempConvertedTextStr, chr(t1),chr(t2),chr(t3)
                    keySuspects.append(t1)
                    keySuspects.append(t2)
                    keySuspects.append(t3)

ttt = 0
sum = 0
for src in convertTextInt :
    temp = keySuspects[ttt]^src
    sum += temp
    ttt +=1 
    if ttt==3 :
        ttt = 0
        
print "Answer : ",sum

"""
(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father. g o d
Answer :  107359
"""