import random
import time
import numpy as np

# TESTCNT = 100000000
TESTCNT = 25000000


def monte_carlo():
    circleIn = 0

    for i in range(TESTCNT):
        # tempX = random.uniform(0, 1)
        # tempY = random.uniform(0, 1)
        tempX = random.random()
        tempY = random.random()

        if (tempX*tempX + tempY*tempY) <= 1:
            circleIn += 1

    print("shot cnt = %f" % (circleIn/TESTCNT))
    print("pi = %f" % (4.0*circleIn/TESTCNT))


startTime = time.time()
monte_carlo()
print("running time : " + str(time.time()-startTime))
