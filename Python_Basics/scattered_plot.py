import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = 2 * x + np.random.randn(50) * 0.2

plt.scatter(x, y, color="purple", edgecolor="black")
plt.title("Feature Correlation Scatter Plot")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.show()
