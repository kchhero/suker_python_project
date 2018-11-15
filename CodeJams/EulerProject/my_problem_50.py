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


# 41 = 2 + 3 + 5 + 7 + 11 + 13
primeL = [ i for i in xrange(3, 1001, 2) if check_prime(i)==True ]
print("prime make done!")
print(len(primeL))
print(primeL)

# maxLength = 0
maxNum = 0
for i in primeL:
    sum = 2
    sum += i
    if sum in primeL:
        if sum > maxNum:
            maxNum = sum
            print("update Largest Num: {}".format(sum))

# #start Num : 7 end Num : 3931 max Length : 543 sum : 997651
