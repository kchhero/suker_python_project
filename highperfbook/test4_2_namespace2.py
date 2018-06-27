from math import sin
import time


def testloop1(iterations):
    result = 0
    for i in range(iterations):
        result += sin(i)
    print(result)


def testloop2(iterations):
    result = 0
    local_sin = sin
    for i in range(iterations):
        result += local_sin(i)
    print(result)


t1 = time.time()
testloop1(100000)
print("testloop1 : %s" % str(time.time()-t1))

t1 = time.time()
testloop2(100000)
print("testloop2 : %s" % str(time.time()-t1))
