
# test function scope
def f():
    a=1
    return a
f()
print(a)

def f():
    b=1
f()
print(b)

c=0
def f():
    c=1
f()
print(c)

def f():
    for i in range(10):
        d = i
f()
print(d, i)

# test block scope
for i in range(10):
    e = i

print(i, e)


#--- concision ---
# python has function scope but no block scope

