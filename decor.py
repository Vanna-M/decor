import time

#run time
def timetest(f):
    def inner(*args):
        t = time.time()
        f(*args)
        t2 = time.time()
        return "execution time: %d seconds"%(t2-t)
    return inner

#name of fxn + args
def whoAmI(f):
    def inner(*args):
        ret = "%s(%s)"%(str(f.func_name),str(*args))
        print ret
        return f(*args)
    return inner

def memoization(f):
    def inner(n):
        fibcache = {}
        if n not in fibcache:
            fibcache[n] = f(n)
        return fibcache[n]
    return inner

#fibonacci sequence but longer
#max 333
#up to 36 in under a minute
@timetest
@memoization
def fib(n):
    if (n <= 1):
        return n
    return fib(n-1) + fib(n-2)


#this is literally a function that wastes time
@timetest
@whoAmI
def timeWaster(n):
    for i in range(n):
        time.sleep(1)

#test
print fib(1)
print fib(5)
print fib(10)
print fib(37)
# print timeWaster(1)
# print timeWaster(5)
# print timeWaster(10)
