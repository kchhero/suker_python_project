listPow = []
for a in range(2,101) :
    for b in range(2,101) :
        listPow.append(pow(a,b))

sortedList = sorted(set(listPow))
print len(sortedList)
print sortedList

