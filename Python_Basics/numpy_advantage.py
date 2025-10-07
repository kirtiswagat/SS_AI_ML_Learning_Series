import time
import numpy as np
# Large dataset
size = 10_000_000
py_list = list(range(size))
np_array = np.arange(size)

# Python list timing
start = time.time()
_ = [x**2 for x in py_list]
print("Python list time:", time.time() - start)

# NumPy array timing
start = time.time()
_ = np_array ** 2
print("NumPy array time:", time.time() - start)