import math

def suker_isPrimeNum(n) :
    if n==2 or n==3 or n==5 or n==7 :
        return 1
    elif n%2==0 :
        return 0
    else :
        sqrtNum = int(math.sqrt(n))
        for i in range(3,sqrtNum+1) :
            if n%i==0 :
                return 0

        return 1

limit = 1000000

suffixPrimeNums = [i*i for i in range(1,int(math.sqrt(limit)))]

end=0
for nn in range(5,limit,2) :
    if end==1 :
        break
    if suker_isPrimeNum(nn)==1:
        pass
    else :
        good=0
        escape=0
        for i in range(3,nn-1,2) :
            if escape==1 :
                break
            if suker_isPrimeNum(i)==1 :                
                for x in range(len(suffixPrimeNums)) :
                    temp = i + 2*suffixPrimeNums[x]
                    if nn == temp  :
                        good=1
                        print nn,"=",i,"+",2,"*",x+1,"^",2
                        escape=1
                        break
                    elif temp > nn :
                        break
                                            
        if good==0 and escape==0:
            print "Answer = ",nn
            end=1
            break

#Answer =  5777
