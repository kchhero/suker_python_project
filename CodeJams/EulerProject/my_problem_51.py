import math
import sys

#1. 같은 자리숫자끼리 그룹핑 100이상부터
#2. 같은 숫자가 2개이상있는 숫자만 골라냄
#3. 몇개의 그룹, 몇개의 숫자인지 파악

primeNo = []
def start() :
    global primeNums
    sukerPrimePath = os.getcwd() + "\\sukerPrimeList.txt"
    if os.path.isfile(sukerPrimePath) :
        primeNo = open(sukerPrimePath, 'r')
        primeNums = primeNo.readline().split(' ')
        #print len(primeNums)
        primeNo.close()
            
def run():
    baseNum = 8
    for i in range(digitCnt-2) :
        for j in range(i+1,digitCnt-1) :
            for p in xrange(startNum,endNum,2) :
                if suker_isPrimeNum(p)==1 :
                    cnt = 0
                    tempStrL = []
                    pStr = str(p)
                    for ll in range(len(pStr)) :
                        tempStrL.append(pStr[ll])               
    
                    for ttt in range(10) :
                        if i==0 and ttt==0 :
                            pass
                        elif ttt>=3 and cnt==0 :#<=(ttt-3) :
                            break
                        else :
                            tempStrL[i] = str(ttt)
                            tempStrL[j] = str(ttt)
                            tempInt = int("".join(tempStrL))
                            
                            if suker_isPrimeNum(tempInt)==1 :
                                cnt += 1
                                #print tempInt,cnt
        
                            if baseNum==cnt :
                                print "Answer :",pStr,i,j
                                sys.exit()
                                
        
suker_getPrimeNum()
run()