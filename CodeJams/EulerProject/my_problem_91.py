import math

boxSize=51
cnt = 0
for x1 in range(boxSize) :
    for y1 in range(boxSize) :
        for x2 in range(boxSize) :
            for y2 in range(boxSize) :
                if x1==x2 and y1==y2 :
                    pass
                elif x1==0 and y1==0 :
                    pass
                elif x2==0 and y2==0 :
                    pass
                else :
                    aa = int(pow(x1,2)+pow(y1,2))
                    bb = int(pow(x2,2)+pow(y2,2))
                    cc = int(pow(x2-x1,2)+pow(y2-y1,2))

                    if cc==aa+bb or bb==aa+cc or aa==bb+cc :
                        print "(",x1,",",y1,")","(",x2,",",y2,")"
                        cnt += 1

print cnt/2
