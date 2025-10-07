import numpy as np
import time
import matplotlib.pyplot as plt

sizes = [10, 100, 1000, 10_000, 100_000, 1_000_000, 10_000_000]
list_times = []
numpy_times = []

for size in sizes:
    # Python list timing
    py_data = list(range(size))
    start = time.perf_counter()
    _ = [x**2 for x in py_data]
    list_times.append(time.perf_counter() - start)

    # NumPy array timing
    np_data = np.arange(size)
    start = time.perf_counter()
    _ = np_data ** 2
    numpy_times.append(time.perf_counter() - start)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(sizes, list_times, label='Python List', marker='o', color='orange')
plt.plot(sizes, numpy_times, label='NumPy Array', marker='s', color='blue')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Array Size')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.show()