import sys
sys.path
sys.path.append('C:/Users/ak66h_000/Dropbox/webscrap/test/python/cython')

def say_hello_to(name):
    print("Hello %s!" % name)

def f(double x):
    return x**2-x

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

from libc.stdlib cimport atoi

cdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "byte string value is NULL"
    return atoi(s)

def f0(int s):
    return s

cdef int cf(int s):
    return s

cpdef int cpf(int s):
    return s

def f1(int s):
    return cf(s)

cpdef int cpf1(int s):
    return cf(s)

def gr(s, s1):
    cdef int g, i
    g = 0
    for i in range(len(s)-1):
        if s[i]*s[i+1] < 0:
            g+=1
            s1[i+1] = g
        else:
            s1[i+1] = g