"""
1~10^5 = (10^5)! = Y1
10^5~10^6 = Y1 * (Y1^9) = Y2
10^6~10^7 = Y2 * (Y2^9) = Y3
10^7~10^8 = Y3 * (Y3^9) = Y4
10^8~10^9 = Y4 * (Y4^9) = Y5
10^9~10^10 = Y5 * (Y5^9) = Y6
10^10~10^11 = Y6 * (Y6^9) = Y7
10^11~10^12 = Y7 * (Y7^9) = Y8
"""

def start() :    
    print "start"
    i = 1
    ss = 1
    while i < 1000000 :
        ss *= i
        ss = int(str(ss).strip('0')[-8:])
        i += 1

   
    y1 = ss # ==> (1~10^5)!
    
    y2 = y1**10
    y2 = int(str(y2).strip('0')[-8:])
        
    y3 = y2**10
    y3 = int(str(y3).strip('0')[-8:])

    y4 = y3**10
    y4 = int(str(y4).strip('0')[-8:])
    
    y5 = pow(y4,10)#y4**9)
    y5 = int(str(y5).strip('0')[-8:])

    y6 = pow(y5,10)#(y5**9)
    y6 = int(str(y6).strip('0')[-8:])

    y7 = pow(y6,10)#(y6**9)
    y7 = int(str(y7).strip('0')[-8:])    
    
#    y8 = pow(y7,10)#(y7**9)
#    y8 = int(str(y8).strip('0')[-8:])
    
    print "Answer : %d" % y7
    
def mainn() :
    start()

if __name__ == "__main__" :
    mainn()
    