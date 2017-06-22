def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(numerator, denominator):
    return float(numerator) / denominator


import sys
data = [ ]
n=10
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0: 3d};Size in bytes: {1: 4d}'.format(a, b))
    data.append(None)