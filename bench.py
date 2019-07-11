import numpy

from time import time

def randomMult():
    x=numpy.random.randint(0, 1e10, (3000,3000))
    y=numpy.random.randint(0, 1e10, (3000,3000))
    return (x @ y).shape

def matInv():
    x=numpy.random.randint(0, 1e10, (3000,3000))
    return (x.linalg.inv()).shape

t = time()
randomMult()
delta = time() - t
print('Multiplication: %0.2fs' % delta)

t = time()
matInv()
delta = time() - t
print('Inversion: %0.2fs' % delta)
