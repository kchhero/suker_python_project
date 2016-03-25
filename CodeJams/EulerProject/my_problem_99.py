import math
import time

lineM = []
lineW = []

try :
    with open("my_problem_99_text.txt") as data :
        for line in data :
            (mM,mW) = line.strip().split(',')
            lineM.append(int(mM))
            lineW.append(int(mW))            
except IOError :
    print "File open error"

maxNum = 0

for i in range(len(lineM)) :
    temp = lineW[i]*math.log10(lineM[i])
    if maxNum < temp :
        maxNum = temp
        print "Max : ", maxNum, i+1, lineM[i],"**",lineW[i]
