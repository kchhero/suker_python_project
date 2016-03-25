import sys,math

limitNum = 1000
squareNumL = [i**2 for i in range(1,int(math.sqrt(limitNum*2)))]
print "squareNumL make done!"

for z in range(1,limitNum) :
    for y in range(z+1,limitNum) :
        for x in range(y+1,limitNum) :
            temp5 = y+z                            
            if temp5 in squareNumL :
                temp6 = y-z
                if temp6 in squareNumL :            
                    temp1 = x+y
                    if temp1 in squareNumL :
                        temp2 = x-y
                        if temp2 in squareNumL :
                            temp3 = x+z
                            if temp3 in squareNumL :
                                print "temp3 ok"
                                temp4 = x-z
                                if temp4 in squareNumL :
                                    print "Answer : x+y+z",x+y+z, x,y,z
                                    sys.exit()