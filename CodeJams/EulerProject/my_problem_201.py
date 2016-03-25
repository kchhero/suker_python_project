"""
import sys

setSL = [i**2 for i in range(1,101)]
print "setSL make done!\n"
uniqueL = []
startNum = 2**50-1
endNum = 2**100
i = startNum

#while i < endNum :
while i < endNum :    
    oneCntL = list(str(bin(i)))
    oneCntL.pop(0)
    oneCntL.pop(0)
    for jj in range(100 - len(oneCntL)) :
        oneCntL.insert(0,'0')
        
    oneCntL.reverse()
    
    if oneCntL.count('1')==50 :
        tempSum = 0
        for k in range(len(oneCntL)) :
            if oneCntL[k] == '1' :
                tempSum += setSL[k]
                
        if tempSum in uniqueL:
            uniqueL.remove(tempSum)
            print "[-] %d"%tempSum
        else :
            uniqueL.append(tempSum)
            print "[+] %d"%tempSum
            
        print "Current ==>%d"%i
    
    i += 1
    
print uniqueL

totalSum = 0
for abc in uniqueL :
    totalSum += int(abc)
    
print "Answer : %d"%totalSum
"""