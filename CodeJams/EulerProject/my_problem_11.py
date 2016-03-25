#line20str = [0]*20
#line20int = [0]*20
line20 = [0]*20
index=0
maxNum=0

#array save
try :
    with open("my_problem_11_text.txt") as data :
        for line in data :
            line20[index] = line.strip().split(' ')
            index = index+1
except IOError :
    print "File open error"
"""
for k1 in range(20) :
    for k2 in range(20) :
        #print int(line20str[k1][k2])
        line20int[k1][k2] = int(line20str[k1][k2])
    """
#processing
#1 colume check
for i in range(20) :
    for j in range(17) :
        temp = int(line20[i][j])*int(line20[i][j+1])*int(line20[i][j+2])*int(line20[i][j+3])
        if maxNum < temp :
            maxNum = temp
        else :
            pass

#2 row check
for i in range(17) :
    for j in range(20) :
        temp = int(line20[i][j])*int(line20[i+1][j])*int(line20[i][j])*int(line20[i+3][j])
        if maxNum < temp :
            maxNum = temp
        else :
            pass

#3 cross1 check
for i in range(17) :
    for j in range(17) :
        temp = int(line20[i][j])*int(line20[i+1][j+1])*int(line20[i+2][j+2])*int(line20[i+3][j+3])
        if maxNum < temp :
            maxNum = temp
        else :
            pass
        
#3 cross1 check
for i in range(17) :
    for j in range(19,2,-1) :
        temp = int(line20[i][j])*int(line20[i+1][j-1])*int(line20[i+2][j-2])*int(line20[i+3][j-3])
        if maxNum < temp :
            maxNum = temp
        else :
            pass

print "maxNum = ",maxNum
