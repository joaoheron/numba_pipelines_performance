from numba import jit
import numpy as np
import time

@jit(nopython=True)
def go_fast(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

@jit(nopython=False)
def go_slow(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

def calc_elapsed_time_jit_c():
    # DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
    x = np.arange(1000000).reshape(1000, 1000)
    start = time.time()
    go_fast(x)
    end = time.time()
    print("Elapsed C (with compilation) = %s" % (end - start))
    # NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
    start = time.time()
    go_fast(x)
    end = time.time()
    print("Elapsed C (after compilation) = %s" % (end - start))

def calc_elapsed_time_jit_python():
    x = np.arange(10000000).reshape(1000, 10000)
    start = time.time()
    go_slow(x)
    end = time.time()
    print("Elapsed python (with compilation) = %s" % (end - start))
    start = time.time()
    go_slow(x)
    end = time.time()
    print("Elapsed python (after compilation) = %s" % (end - start))
    