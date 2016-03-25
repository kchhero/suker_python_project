import math

def cardano(a=1,b=1,c=1) :
    return (a+b*math.sqrt(c))**(1/3) + (a-b*math.sqrt(c))**(1/3)
    
print cardano(2,1,5)