import time


def myxrange(start, stop, step=1):
    while start < stop:
        yield start
        start += step

        
def test_range():
    for _ in range(1, 100000000):
        pass


def test_xrange():
    for _ in xrange(1, 100000000):
        pass


@profile
def test_list_comprehension(list_of_numbers):
    divisible_by_three = len([n for n in list_of_numbers if n % 3 == 0])
    print(divisible_by_three)


@profile
def test_gen_comprehension(list_of_numbers):
    divisible_by_three = sum((1 for n in list_of_numbers if n % 3 == 0))
    print(divisible_by_three)


ff = myxrange(1,5000000)

#t1 = time.time()
test_list_comprehension(ff)
#print("test_list_comprehension time : " + str(time.time()-t1))

#t2 = time.time()
test_gen_comprehension(ff)
#print("test_gen_comprehension time : " + str(time.time()-t2))

# t1 = time.time()
# test_range()
# print("test_range time : " + str(time.time()-t1))

# t2 = time.time()
# test_xrange()
# print("test_xrange time : " + str(time.time()-t2))
