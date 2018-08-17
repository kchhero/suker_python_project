symmetryList = []


def symmetry():
    for i in range(1, 1000000):
        if str(i) == str(i)[::-1]:
            symmetryList.append(i)


def anal():
    cnt = 0
    tsum = 0
    for i in symmetryList:
        __bin = bin(i)[2:]
        if str(__bin) == str(__bin)[::-1]:
            cnt += 1
            tsum += i
            print("2b : {} ,  10d : {}".format(__bin, i))

    print("sum = %d" % tsum)


symmetry()
anal()
