sum = 0
cnt = 0
#i = 1023456789
i = 1406357289
while i < 9876543211 :
    tempStr = str(i)
    tempL = [tempStr[k] for k in range(10)]
    if len(tempL)==len(set(tempL)) :
        if int(tempStr[3])%2==0 and int(tempStr[5])%5==0 :
            tt1 = []
            tt1.append(tempStr[2])
            tt1.append(tempStr[3])
            tt1.append(tempStr[4])
            if (int("".join(tt1)))%3==0 :    
                tt2 = []
                tt2.append(tempStr[4])
                tt2.append(tempStr[5])
                tt2.append(tempStr[6])
                if (int("".join(tt2)))%7==0 :    
                    tt3 = []
                    tt3.append(tempStr[5])
                    tt3.append(tempStr[6])
                    tt3.append(tempStr[7])
                    if (int("".join(tt3)))%11==0 :    
                        tt4 = []
                        tt4.append(tempStr[6])
                        tt4.append(tempStr[7])
                        tt4.append(tempStr[8])                        
                        if (int("".join(tt4)))%13==0 :    
                            tt5 = []
                            tt5.append(tempStr[7])
                            tt5.append(tempStr[8])
                            tt5.append(tempStr[9])
                            if (int("".join(tt5)))%17==0 :
                                print i
                                sum += i

    i += 9
    cnt += 1
    if cnt==10000000 :
        cnt = 0
        print "doing...",i
print "sum = ",sum

#sum =  16695334890