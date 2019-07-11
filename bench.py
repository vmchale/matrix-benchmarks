import numpy as np

from time import time

print(np.__config__.show())

def randomMult():
    x=np.random.randint(0, 1e10, (3000,3000))
    y=np.random.randint(0, 1e10, (3000,3000))
    return (x @ y)


def matInv():
    x=np.random.randint(0, 1e10, (3000,3000))
    return np.linalg.inv(x)

t = time()
_ = matInv()
delta = time() - t
print('Inversion: %0.2fs' % delta)

t = time()
_ = randomMult()
delta = time() - t
print('Multiplication: %0.2fs' % delta)
