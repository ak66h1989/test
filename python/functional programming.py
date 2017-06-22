def f(i):
    while i>3:
        return
    print(i)
    f(i+1)
    print(i)

f(1)

def curry(prior, *additional):
    def curried(*args):
        return prior(*(additional+args))
    return curried

def add(x, y, z):
    return x+y+z
add(1,2,3)
c = curry(add,1)
c1=curry(c,2)
c1(3)

def add(*args):
    return sum(args)
c = curry(add,1)
c1 = curry(c, 2)
c(2,3,4)
c1(3,4)

def add(a,*args):
    print(args, a)

add(1,2,3)
