
from pandas import *
from numpy import *
import timeit
df = DataFrame({'a': np.random.randn(1000),'b': np.random.randn(1000),'N': np.random.randint(100, 1000, (1000)),'x': 'x'})

df = DataFrame({'a': np.random.randn(1000),'b': np.random.randn(1000),'N': np.random.randint(100, 1000, (1000))})

df.apply(sum, axis=0)
df.apply(sum, axis=1)
df.apply(lambda y: y+100, axis=0)
df[['N']].apply(lambda y: 1, axis=1)

for i in range(len(df)):
    df['N'][i] = 1
df['N']

%load_ext Cython

def f_plain(x):
    return x * (x - 1)
def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_plain(a + i * dx)
    return s * dx

f_plain(3)

%timeit df.apply(lambda x: integrate_f(x['a'], x['b'], x['N']), axis=1)
%prun -l 4 df.apply(lambda x: integrate_f(x['a'], x['b'], x['N']), axis=1)

%%cython
def f_plain(x):
    return x * (x - 1)
def integrate_f_plain(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_plain(a + i * dx)
    return s * dx

%timeit df.apply(lambda x: integrate_f_plain(x['a'], x['b'], x['N']), axis=1)
%prun -l 4 df.apply(lambda x: integrate_f_plain(x['a'], x['b'], x['N']), axis=1)

%%cython
cdef double f_typed(double x) except? -2:
    return x * (x - 1)
cpdef double integrate_f_typed(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f_typed(a + i * dx)
    return s * dx

%timeit df.apply(lambda x: integrate_f_typed(x['a'], x['b'], x['N']), axis=1)
%prun -l 4 df.apply(lambda x: integrate_f_typed(x['a'], x['b'], x['N']), axis=1)

import sys
sys.path
sys.path.append('C:/Users/ak66h_000/Dropbox/webscrap/test/python/cython')
from hello import *

say_hello_to('1234')

def f(s):
    return s

f(100)
f0(100)
f1(100)
cpf(100)
cf(10)
parse_charptr_to_py_int('a')

%timeit f(100)
%timeit f0(100)
%timeit cpf(100)
%timeit f1(100)
%timeit cpf1(100)

def f():
    print(abc)
abc=1
'中文'.encode('big5').decode('big5')
type('中文'.encode('big5').decode('big5'))