def triNum(n) :
    return n*(n+1)/2

lineTextL = []
lineTextTriL = []
triNumL = []
index = 0
try :
    with open("my_problem_42_text.txt") as data :
        for line in data :
            lineTextL = line.strip().split(',')
            
except IOError :
    print "File open error"

for i in range(len(lineTextL)+2) :
    triNumL.append(triNum(i))

print triNumL

cnt = 0
for t in lineTextL :
    localSum = 0
    for i in range(len(t)) :
        localSum += ord(t[i])-64

    #lineTextTriL.append(localSum)
    if localSum in triNumL :
        cnt += 1
        print localSum, t

print "Answer : ",cnt
