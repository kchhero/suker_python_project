line100 = [0]*100
sum=0
index=0

#array save
try :
    with open("my_problem_13_text.txt") as data :
        for line in data :
            line100[index] = line.strip()
            print line100[index]
            index = index+1
            
except IOError :
    print "File open error"

for i in range(100) :    
     sum = sum + int(line100[i])

print sum
print "first 10 digit = ", sum
