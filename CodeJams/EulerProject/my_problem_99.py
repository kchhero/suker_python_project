import math

lineM = []
lineW = []
maxNum = 0

try:
    with open("my_problem_99_text.txt") as data:
        for line in data:
            (mM, mW) = line.strip().split(',')
            lineM.append(int(mM))
            lineW.append(int(mW))
except IOError:
    print("File open error")

maxNum = 0
print("start calculate")

for i in range(len(lineM)):
    temp = lineW[i]*math.log10(lineM[i])
    if maxNum < temp:
        maxNum = temp
        print("Update MaxNum : {}, line : {}".format(maxNum, i+1))
