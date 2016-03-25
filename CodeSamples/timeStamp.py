import nlib

def timef(f, ns=1000, dt=60):
    import time
    t=t0=time.time()
    for k in xrange(1,ns):
    	f()
	t=time.time()
	if t-t0>dt : break
    return (t-t0)/k

@memoize
def fib(n) :
    return n if n<2 else fib(n-1)+fib(n-2)

for k in range(15,20):
    print k, timef(lambda:fib(k))
