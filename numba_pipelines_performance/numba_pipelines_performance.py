from numba import jit
import numpy as np
import time

x = np.arange(10000).reshape(100, 100)

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

# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed C (with compilation) = %s" % (end - start))

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed C (after compilation) = %s" % (end - start))

start = time.time()
go_slow(x)
end = time.time()
print("Elapsed python (with compilation) = %s" % (end - start))

start = time.time()
go_slow(x)
end = time.time()
print("Elapsed python (after compilation) = %s" % (end - start))