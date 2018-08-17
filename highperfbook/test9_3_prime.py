import math
import time


def check_prime(n):
    if n % 2 == 0:
        return False

    startNum = 3
    endNum = (int)(math.sqrt(n) + 1)
    for i in range(startNum, endNum, 2):
        if n % i == 0:
            return False

    return True


st = time.time()

for i in range(1000000):
    if check_prime(i) is True:
        print(i),

print("Run Time : {}".format(time.time()-st))
