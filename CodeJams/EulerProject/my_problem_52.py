for i in xrange(1,999999) :
    d1 = str(i)
    d2 = str(i*2)
    d3 = str(i*3)
    d4 = str(i*4)
    d5 = str(i*5)
    d6 = str(i*6)

    baseLen = len(d1)
    if baseLen==len(d2) and baseLen==len(d3) and baseLen==len(d4) and baseLen==len(d5) and baseLen==len(d6) :
        tempL1 = [d1[j] for j in range(baseLen)]
        tempL2 = [d2[j] for j in range(baseLen)]
        tempL3 = [d3[j] for j in range(baseLen)]
        tempL4 = [d4[j] for j in range(baseLen)]
        tempL5 = [d5[j] for j in range(baseLen)]
        tempL6 = [d6[j] for j in range(baseLen)]
        
        tempL1.sort()
        tempL2.sort()
        tempL3.sort()
        tempL4.sort()
        tempL5.sort()
        tempL6.sort()
        
        if "".join(tempL1)=="".join(tempL2) and "".join(tempL2)=="".join(tempL3) and \
           "".join(tempL3)=="".join(tempL4) and "".join(tempL4)=="".join(tempL5) and \
           "".join(tempL5)=="".join(tempL6) :
            print i,d2,d3,d4,d5,d6
            break



