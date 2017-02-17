from collections import deque
import time

def dequeTest() :
    startTime = time.time()
    q = deque()
    for i in range(40000000) :
        q.append(i)

    while len(q)!=0 :
        q.pop()

    print "deque time : %.5f"%(time.time() - startTime)


def listTest() :
    startTime = time.time()
    ll = []

    for i in range(40000000) :
        ll.append(i)

    while len(ll)!=0 :
        ll.pop(-1)

    print "list time : %.5f"%(time.time() - startTime)

dequeTest()
listTest()
                        
