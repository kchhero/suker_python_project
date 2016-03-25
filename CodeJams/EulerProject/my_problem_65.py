#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]
#1 => 2, 3
#2 => 4, 6
#3 => 6, 9
#33 => 66, 99
#100 digit => 1
#therefore ==>  #e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ..., 1,66,1]

e = [2]
def start() :
    global e    
    cnt = 1
    for i in range(2, 101) :
        if i%3!=0 :
            e.append(1)
        else :
            e.append(cnt*2)
            cnt += 1
            
def cal(before) :
    global e
    if len(e)==1 :
        ansUp = e.pop(-1)*before[1]+before[0]
        ansDown = before[1]
        print "Answer : %d/%d"%(ansUp,ansDown)
        ttt = str(ansUp)
        kk = 0
        for j in range(len(ttt)) :
            kk += int(ttt[j])
        print "Answer of Answer : %d"%kk
        return    
    temp = [e.pop(-1)*before[1] + before[0], before[1]]
    reCalTemp = [temp[1], temp[0]]
    cal(reCalTemp)

if __name__ == "__main__" :
    start()
    temp = [1, e.pop(-1)]
    before = [e.pop(-1)*temp[1] + temp[0], temp[1]]
    reCalBefore = [before[1], before[0]]
    cal(reCalBefore)

"""
Answer : 6963524437876961749120273824619538346438023188214475670667/2561737478789858711161539537921323010415623148113041714756
Answer of Answer : 272
"""