import time
import numpy as np


def timer(f):
    def mod(*args, **kwargs):
        start = time.time()
        val = f(*args, **kwargs)
        fin = time.time()
        print(f"time difference for function: {f.__name__} is: {fin-start}")
        return val
    return mod


@timer
class thing():
    def __init__(self):
        print("I'm alive!")
        self._makeTimer()

    def _makeTimer(self):
        start = time.time()
        print("hi there")
        fin = time.time()
        print(f"time difference is: {fin-start}")


@timer
def dot_product(x,y): 
    sc = np.asarray(list(zip(x,y)))
    return np.array([i*j for (i,j) in sc ])

if __name__ == "__main__":
    # timer for the constructor of a class
    a = thing()

    # use a function with a return value and time it too!
    x = np.arange(1,10000,2)
    y = np.arange(1,10000,3)
    z = dot_product(x,y)
