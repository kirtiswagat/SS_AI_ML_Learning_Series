import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)
plt.boxplot(data)
plt.title("Boxplot Example")
plt.ylabel("Values")
plt.show()
