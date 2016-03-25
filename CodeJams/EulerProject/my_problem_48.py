sum = 0
for i in range(1,1001) :
    sum += pow(i,i)%pow(10,10)

print sum%pow(10,10)
