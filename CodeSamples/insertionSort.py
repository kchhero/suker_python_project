import random

def insertion_sort(A):
    for i in xrange(1,len(A)):
    	for j in xrange(i,0,-1):
	    if A[j] < A[j-1] :
	      A[j],A[j-1] = A[j-1],A[j]
	    else : break

def test():
    a=[random.randint(0,100) for k in xrange(20)]
    insertion_sort(a)
    print a

test()
