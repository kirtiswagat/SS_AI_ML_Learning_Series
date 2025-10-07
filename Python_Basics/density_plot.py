import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)
plt.figure(figsize=(7,4))
plt.hist(data, bins=30, density=True, alpha=0.6, color='green')
plt.title("Density Plot (PDF Approximation)")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()
