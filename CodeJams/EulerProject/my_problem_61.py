num3L = []
num4L = []
num5L = []
num6L = []
num7L = []
num8L = []
ttL = []

swt = [False]*6

def num3(n) :
    return n*(n+1)/2
def num4(n) :
    return n*n
def num5(n) :
    return n*(3*n-1)/2
def num6(n) :
    return n*(2*n-1)
def num7(n) :
    return n*(5*n-3)/2
def num8(n) :
    return n*(3*n-2)

def start() :
    global num3L
    global num4L
    global num5L
    global num6L
    global num7L
    global num8L
    global ttL
    
    for i in range(10,200) :
        temp = num3(i)
        if temp >= 1000 and temp <= 9999 :
            num3L.append(temp)
    
        temp = num4(i)
        if temp >= 1000 and temp <= 9999 :
            num4L.append(temp)
    
        temp = num5(i)
        if temp >= 1000 and temp <= 9999 :
            num5L.append(temp)
    
        temp = num6(i)
        if temp >= 1000 and temp <= 9999 :
            num6L.append(temp)
    
        temp = num7(i)
        if temp >= 1000 and temp <= 9999 :
            num7L.append(temp)
    
        temp = num8(i)
        if temp >= 1000 and temp <= 9999 :
            num8L.append(temp)
    
  #  ttL = [num3L, num4L, num5L, num6L, num7L, num8L]
    
def checknumL(j) :
    if j in num3L :
        if swt[0]==True :
            return -1
        else :
            swt[0] = True
            return 3
    elif j in num4L :
        if swt[1]==True :
            return -1
        else :
            swt[1] = True
            return 4
    elif j in num5L :
        if swt[2]==True :
            return -1
        else :
            swt[2] = True
            return 5
    elif j in num6L :
        if swt[3]==True :
            return -1
        else :
            swt[3] = True
            return 6
    elif j in num7L :
        if swt[4]==True :
            return -1
        else :
            swt[4] = True
            return 7
    elif j in num8L :
        if swt[5]==True :
            return -1
        else :
            swt[5] = True
            return 8
    else :
        return -1
    
def mainn(t) :
    global swt
    for i in ttL[t-3] :
        org = i
        step1 = (i%100)*100
        for j in range(step1,step1+100) :
            ret = checknumL(j)
            if ret==-1 :
                swt = [False]*6
                break
        
    mainn(ret)
    print "END---"

if __name__ == "__main__" :
    start()
    mainn(3)







