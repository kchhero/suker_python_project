maxTriNum = 0
pp = [0]*1000

for a in range(1,1000) :    
    for b in range(1,1000) :
        for c in range(1,1000) :
            if c < b and c < a :
                pass
            elif b < a :
                pass
            elif (a+b+c) < 1000 :
                if pow(c,2)==(pow(a,2)+pow(b,2)) :
                    temp = pp[a+b+c]
                    pp[a+b+c] = temp+1
                    print "a,b,c = ",a,b,c
                    print "pp and sum",pp[a+b+c], a+b+c

temp = max(pp)
for i in range(1000) :
    if temp==pp[i] :
        print i
