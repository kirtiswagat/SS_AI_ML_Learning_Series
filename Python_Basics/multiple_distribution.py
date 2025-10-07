import numpy as np
import matplotlib.pyplot as plt
data1 = np.random.normal(50, 10, 1000)
data2 = np.random.normal(60, 15, 1000)

plt.hist(data1, bins=30, alpha=0.5, label="Group A")
plt.hist(data2, bins=30, alpha=0.5, label="Group B")
plt.legend()
plt.title("Comparing Two Data Distributions")
plt.show()
