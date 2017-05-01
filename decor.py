import time

#run time
def timetest(f):
    def inner(*args):
        t = time.time()
        f(*args)
        t2 = time.time()
        return "execution time: %d"%(t2-t)
    return inner

#name of fxn + args
def whoAmI(f):
    def inner(*args):
        ret = "%s(%s)"%(str(f.func_name),str(*args))
        #this has to happen for the output to match Mr. Brown's
        f(*args)
        print ret
        return ret
    return inner

#fibonacci sequence but longer
@timetest
@whoAmI
def fib(n):
    if (n <= 1):
        return n
    time.sleep(.5)
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
print timeWaster(1)
print timeWaster(5)
print timeWaster(10)
