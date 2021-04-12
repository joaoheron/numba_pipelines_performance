from numba import jit
import numpy as np
import time

@jit(nopython=True)
def trace_numpy_c(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

@jit(nopython=False)
def trace_numpy_python(a): # Function is compiled and runs in machine code
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

@jit(nopython=True)
def for_loop_c(nu):
    total = 0
    for n in range(nu):
        total += nu
    return total

@jit(nopython=False)
def for_loop_python(nu):
    total = 0
    for n in range(nu):
        total += nu
    return total

def calc_elapsed_time_numpy_jit_c():
    # DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
    x = np.arange(1000000000).reshape(100000, 10000)
    start = time.time()
    trace_numpy_c(x)
    end = time.time()
    print("Elapsed C (with compilation) = %s" % (end - start))
    # NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
    start = time.time()
    trace_numpy_c(x)
    end = time.time()
    print("Elapsed C (after compilation) = %s" % (end - start))

def calc_elapsed_time_numpy_jit_python():
    x = np.arange(1000000000).reshape(100000, 10000)
    start = time.time()
    trace_numpy_python(x)
    end = time.time()
    print("Elapsed python (with compilation) = %s" % (end - start))
    start = time.time()
    trace_numpy_python(x)
    end = time.time()
    print("Elapsed python (after compilation) = %s" % (end - start))

def calc_elapsed_time_loop_jit_c():
    nu = 1000000000000
    start = time.time()
    for_loop_c(nu)
    end = time.time()
    print("Elapsed C (with compilation) = %s" % (end - start))
    start = time.time()
    for_loop_c(nu)
    end = time.time()
    print("Elapsed C (after compilation) = %s" % (end - start))

def calc_elapsed_time_loop_jit_python():
    nu = 1000000000000
    start = time.time()
    for_loop_python(nu)
    end = time.time()
    print("Elapsed python (with compilation) = %s" % (end - start))
    start = time.time()
    for_loop_python(nu)
    end = time.time()
    print("Elapsed python (after compilation) = %s" % (end - start))
