import time

def test1(x):
    total = 0
    for i in range(x):
        total += 1

    return total


def test2(x):
    total = 0
    for _ in range(x):
        total += 1

    return total



t2 = time.time()
print("test2 val: %d" % test2(1000000) + "time : " + str(time.time()-t2))
t1 = time.time()
print("test1 val: %d" % test1(1000000) + "time : " + str(time.time()-t1))
